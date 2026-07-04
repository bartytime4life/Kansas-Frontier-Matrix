# `schemas/contracts/v1/focus/` — Focus Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-focus-readme
title: schemas/contracts/v1/focus/ — Focus Schema Family Index
type: readme; schema-family-index; focus-mode-governance-boundary; ui-runtime-trust-membrane
owner_class: schema-family
version: v0.1
status: draft; schema-stubs-present; PROPOSED; path-family-present; ui-schema-overlap-visible; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Focus Mode steward
  - OWNER_TBD — UI steward
  - OWNER_TBD — Governed API steward
  - OWNER_TBD — Governed AI/runtime steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; focus; focus-mode; FocusRequest; FocusResponse; RuntimeResponseEnvelope; CitationValidationReport; governed-api; governed-ai; finite-outcomes; trust-membrane; evidence-bound; policy-bound; release-gated; no-sovereign-truth
tags: [kfm, schemas, contracts, v1, focus, FocusRequest, FocusResponse, RuntimeResponseEnvelope, CitationValidationReport, FocusModePayload, EvidenceBundle, EvidenceRef, PolicyDecision, AIReceipt, governed-api, governed-ai, finite-outcomes, ANSWER, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ./focus_request.schema.json
  - ./focus_response.schema.json
  - ./runtime_response_envelope.schema.json
  - ./citation_validation_report.schema.json
  - ../../../../contracts/ui/focus_request.md
  - ../../../../contracts/ui/focus_response.md
  - ../../../../contracts/focus_mode/
  - ../../../../contracts/runtime/
  - ../../../../contracts/evidence/
  - ../../../../contracts/policy/
  - ../../../../docs/architecture/ui/FOCUS_FLOW.md
  - ../../../../docs/architecture/governed-ai/README.md
  - ../../../../docs/architecture/governed-api.md
  - ../../../../policy/focus/
  - ../../../../policy/ui/
  - ../../../../policy/runtime/
  - ../../../../policy/evidence/
  - ../../../../fixtures/focus/
  - ../../../../tests/focus/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/focus/README.md."
  - "Current GitHub search surfaced focus_request.schema.json, focus_response.schema.json, runtime_response_envelope.schema.json, and citation_validation_report.schema.json under this folder."
  - "Opened focus schema files are permissive PROPOSED scaffolds with empty properties and additionalProperties true."
  - "contracts/ui/focus_request.md and contracts/ui/focus_response.md refer to paired UI schema paths under schemas/contracts/v1/ui/, while this folder also contains focus_request and focus_response schema stubs; this overlap is recorded as NEEDS VERIFICATION."
  - "Focus output must remain downstream of evidence, policy, citation validation, release state, correction posture, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-focus-purple)
![shape](https://img.shields.io/badge/authority-machine--shape-informational)
![maturity](https://img.shields.io/badge/maturity-PROPOSED-orange)
![outcomes](https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-blue)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/focus/` is the machine-checkable schema family for Focus Mode request/response and governed-runtime-facing focus envelopes.
>
> **One-line boundary.** This folder defines focus object **shape**. It does not implement Focus Mode, call AI/model runtimes, decide evidence truth, grant policy permission, approve releases, store Focus payloads, or authorize public answers.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current schema inventory](#current-schema-inventory) · [Known overlap and drift risks](#known-overlap-and-drift-risks) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Schema-family rules](#schema-family-rules) · [Trust membrane guardrails](#trust-membrane-guardrails) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/focus/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are focus schema files present in this folder? | Yes. Search surfaced four schema files under `schemas/contracts/v1/focus/`. | **CONFIRMED path presence** |
| Are opened focus schemas mature/field-complete? | No. Opened files are permissive `PROPOSED` scaffolds with empty `properties` and `additionalProperties: true`. | **CONFIRMED / NEEDS IMPLEMENTATION** |
| Is there related UI contract prose? | Yes. `contracts/ui/focus_request.md` and `contracts/ui/focus_response.md` exist. | **CONFIRMED** |
| Is schema placement fully settled? | Not entirely. UI contracts reference `schemas/contracts/v1/ui/...`, while this folder contains similarly named focus schema stubs. | **NEEDS VERIFICATION / drift-sensitive** |
| Can these schemas alone authorize a Focus answer? | No. Focus output requires governed API/runtime, evidence, citation, policy, release, correction, and rollback support. | **CONFIRMED governance boundary** |

> [!IMPORTANT]
> Focus Mode must preserve finite outcomes: `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`. A schema-valid response is not proof that an answer is true, public-safe, policy-allowed, or release-ready.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/focus/
```

It may define machine-checkable Focus Mode shapes, but adjacent authority is split:

- `contracts/ui/` owns UI-facing meaning for request/response projection contracts.
- `contracts/focus_mode/` should own Focus Mode payload meaning where implemented and verified.
- `contracts/runtime/` owns runtime envelope and decision meaning.
- `contracts/evidence/` owns EvidenceBundle, EvidenceRef, and citation semantics.
- `contracts/policy/` and `policy/` own policy decision meaning and enforcement posture.
- `docs/architecture/ui/FOCUS_FLOW.md` describes UI-side Focus Flow behavior and invariants.
- Governed API/runtime implementation belongs outside schemas.
- `fixtures/` and `tests/` prove valid/invalid behavior.
- `release/` owns public release, correction, withdrawal, and rollback decisions.

This README does not amend ADR-0001, Directory Rules, UI contracts, runtime contracts, evidence contracts, policy, validators, or release doctrine.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        └── focus/
            ├── README.md                              # this file
            ├── focus_request.schema.json              # PROPOSED permissive scaffold
            ├── focus_response.schema.json             # PROPOSED permissive scaffold
            ├── runtime_response_envelope.schema.json  # PROPOSED permissive scaffold
            └── citation_validation_report.schema.json # PROPOSED permissive scaffold

contracts/
├── ui/
│   ├── focus_request.md                               # UI request semantic contract
│   └── focus_response.md                              # UI response semantic contract
├── focus_mode/                                        # Focus payload meaning; maturity NEEDS VERIFICATION
├── runtime/                                           # runtime envelope / decision / AI receipt meaning
├── evidence/                                          # EvidenceBundle / EvidenceRef / citation meaning
└── policy/                                            # policy decision meaning

policy/
├── focus/
├── ui/
├── runtime/
└── evidence/

fixtures/
tests/
release/
```

---

## Current schema inventory

Current GitHub search surfaced the following files under `schemas/contracts/v1/focus/`. This is a search-derived index, not a complete mounted-checkout manifest.

| File | Current opened signal | Status |
|---|---|---|
| `focus_request.schema.json` | Draft 2020-12 object; empty `properties`; `additionalProperties: true`; `x-kfm.status: PROPOSED`; source doc points to Archaeology map UI contracts. | **PROPOSED scaffold** |
| `focus_response.schema.json` | Draft 2020-12 object; empty `properties`; `additionalProperties: true`; `x-kfm.status: PROPOSED`; source doc points to Archaeology map UI contracts. | **PROPOSED scaffold** |
| `runtime_response_envelope.schema.json` | Draft 2020-12 object; empty `properties`; `additionalProperties: true`; `x-kfm.status: PROPOSED`; source doc points to Hazards API contracts. | **PROPOSED scaffold** |
| `citation_validation_report.schema.json` | Draft 2020-12 object; empty `properties`; `additionalProperties: true`; `x-kfm.status: PROPOSED`; source doc points to Archaeology map UI contracts. | **PROPOSED scaffold** |

> [!NOTE]
> These files confirm path presence and scaffold intent. They do not confirm final field shape, validator behavior, fixture coverage, policy enforcement, runtime routing, UI rendering, release readiness, or public-safe behavior.

---

## Known overlap and drift risks

| Risk | Evidence | Required posture |
|---|---|---|
| Focus request/response schema home overlap | `contracts/ui/focus_request.md` and `contracts/ui/focus_response.md` point to paired UI schema paths under `schemas/contracts/v1/ui/`, while similarly named stubs exist in `schemas/contracts/v1/focus/`. | Do not let both families become parallel authorities. Resolve with schema steward review or ADR/migration note. |
| Runtime envelope duplication | `runtime_response_envelope.schema.json` exists under `focus/`, but runtime authority belongs with runtime contracts/schemas if the envelope is general-purpose. | Decide whether this is a Focus-profile of a runtime envelope or misplaced runtime schema. |
| Citation validation duplication | `citation_validation_report.schema.json` exists under `focus/`, while citation validation also belongs near evidence/UI families. | Decide whether this is a Focus-specific projection or duplicate shared evidence schema. |
| Domain-source scaffolding | Current stubs were generated from domain docs such as Archaeology and Hazards surfaces. | Promote only after cross-domain Focus semantics and contracts are reviewed. |

---

## What belongs here

- This README.
- Focus-family JSON Schema files after schema/contract review.
- Focus-specific request/response profiles that are not better owned by `ui/`, `runtime/`, `evidence/`, or `focus_mode/`.
- Focus-specific schema migration notes, mirror notes, deprecation notes, and drift notes.
- Links to paired contracts, fixtures, validators, policy references, EvidenceBundle/CitationValidationReport references, AIReceipt references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- UI semantic contract prose.
- Runtime/API implementation code.
- AI/model prompts, direct model outputs, embedding/vector/graph calls, or runtime traces.
- EvidenceBundle instances, source payloads, catalog records, proof outputs, receipt instances, release records, correction notices, or rollback cards as emitted data.
- Policy rules, sensitivity decisions, redaction decisions, or exposure decisions.
- Public map layers, tiles, screenshots, dashboards, Focus Mode generated answers, or user-facing summaries.
- Claims that Focus output is true or public-safe merely because it validates against a schema.

---

## Schema-family rules

| Rule | Requirement |
|---|---|
| Finite outcomes | Every Focus response path must preserve `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` without silent degradation. |
| Governed API boundary | Focus requests must target governed interfaces, not direct model runtime, graph, vector, object, RAW, WORK, QUARANTINE, or internal canonical stores. |
| PUBLISHED-only context | UI-built context should reference released layers, released time snapshots, and governed catalog feature IDs. |
| Evidence dependency | `ANSWER` output must carry evidence/citation support or abstain/deny/error. |
| Policy dependency | Missing or failed policy checks should produce `DENY`, `ABSTAIN`, or `ERROR`, not answer text. |
| Citation dependency | CitationValidationReport must not launder missing or weak evidence into an answer. |
| Sensitivity dependency | Sensitive coordinates, archaeology, rare species, living-person/DNA/land joins, infrastructure-sensitive data, and other protected details require redaction/generalization/denial. |
| Release dependency | Public/exported Focus output must respect release, correction, and rollback state. |
| AI humility | AI output is downstream carrier text, not sovereign truth. |
| No parallel authority | Do not duplicate UI/runtime/evidence/policy schema authority under `focus/` without ADR or migration notes. |

---

## Trust membrane guardrails

A mature Focus flow should preserve this boundary:

```text
UI interaction
  -> FocusRequest / map context / caller role
  -> governed API
  -> evidence + policy + citation + release checks
  -> runtime / AI adapter only if allowed
  -> RuntimeResponseEnvelope: ANSWER | ABSTAIN | DENY | ERROR
  -> FocusResponse / FocusModePayload / EvidenceDrawerPayload projection
  -> public-safe UI render with trust-visible state
```

Required deny/abstain/error posture:

| Condition | Expected outcome posture |
|---|---|
| Evidence unresolved | `ABSTAIN`, `DENY`, or `ERROR`; never uncited `ANSWER`. |
| Citation validation fails | `ABSTAIN`, `DENY`, or `ERROR`; never hidden failure. |
| Policy missing or failed | `DENY` or `ERROR`; fail closed. |
| Sensitive geometry requested | `DENY`, `RESTRICT`, `GENERALIZE`, or `ABSTAIN`; no exact leak. |
| Release state missing for public output | `DENY` or non-public review-only output. |
| Direct model/runtime/internal-store access requested | `DENY` or `ERROR`; normal public path uses governed interfaces. |
| AI text contradicts EvidenceBundle | EvidenceBundle and policy posture win; answer must abstain, deny, or expose contradiction state. |

---

## Promotion checklist

A focus schema should not advance beyond `PROPOSED` unless:

- [ ] Schema family placement is settled against `ui/`, `runtime/`, `evidence/`, and `focus_mode/` schema homes.
- [ ] Paired semantic contract exists and matches schema path.
- [ ] `$id` and filename are stable.
- [ ] JSON Schema dialect is pinned.
- [ ] Required fields are defined.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validator implementation exists.
- [ ] CI/schema-test support exists.
- [ ] Finite outcome behavior is fixture-tested.
- [ ] Evidence/citation/policy/release dependencies are fixture-tested.
- [ ] Sensitive denial/redaction/generalization cases are fixture-tested.
- [ ] Governed API route and UI rendering behavior are verified or explicitly out of scope.
- [ ] Correction and rollback references are clear for public/exported output.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect current focus schema family.
find schemas/contracts/v1/focus -maxdepth 2 -type f | sort

# Search for overlapping Focus authority in UI/runtime/evidence/focus-mode schema families.
find schemas/contracts/v1 contracts docs policy fixtures tests -maxdepth 6 -type f \
  | grep -Ei 'focus|runtime_response_envelope|citation_validation_report|FocusRequest|FocusResponse|FocusModePayload' \
  | sort

# Validate JSON syntax for current focus schemas.
find schemas/contracts/v1/focus -name '*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/ui tests/focus tests/runtime tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/focus/README.md`.

Rollback for future Focus schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore governed API, UI, Focus Mode payload, Evidence Drawer, and runtime adapter consumers.
6. Restore policy/evidence/citation/release references.
7. Preserve correction and rollback records if public Focus outputs were affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should `focus_request.schema.json` and `focus_response.schema.json` live under `focus/`, `ui/`, or both with a clear profile/mirror rule? | **NEEDS VERIFICATION / ADR-sensitive** | Schema steward + UI steward + Focus steward |
| Is `runtime_response_envelope.schema.json` a Focus-specific profile or should it live under runtime schemas? | **NEEDS VERIFICATION** | Runtime steward + schema steward |
| Is `citation_validation_report.schema.json` a Focus-specific projection or duplicate shared evidence/citation schema? | **NEEDS VERIFICATION** | Evidence steward + schema steward |
| Which fields are required for FocusRequest and FocusResponse? | **NEEDS VERIFICATION** | Focus steward + UI steward |
| Which fixtures prove finite outcomes and deny-by-default behavior? | **NEEDS VERIFICATION** | Validation steward |
| Which Focus outputs are safe for public UI, export, and Focus Mode county plans? | **NEEDS VERIFICATION / release-gated** | Release steward + policy steward |

---

## Maintainer notes

- Treat current focus schemas as permissive scaffolds until fields, fixtures, validators, and CI are verified.
- Resolve overlap with `schemas/contracts/v1/ui/`, runtime, evidence, and focus-mode schema homes before promotion.
- Preserve finite outcomes, cite-or-abstain, governed API boundaries, release state, correction path, and rollback support.
- Never let Focus Mode become a direct AI answer path around evidence and policy.
