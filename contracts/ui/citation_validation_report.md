<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-citation-validation-report
title: contracts/ui/citation_validation_report.md — UI CitationValidationReport Contract
type: semantic-contract; ui-projection-profile
version: v0.2
status: draft; PROPOSED; schema-stub-confirmed; ui-family; citation-report-projection; evidence-dependent; not-evidence-closure
owners: OWNER_TBD — UI steward · Evidence steward · Citation/source steward · Contracts steward · Schema steward · Policy steward · Release steward · Accessibility steward · Docs steward
created: NEEDS VERIFICATION — greenfield scaffold existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; ui; citation-validation-report; citation-checking; evidence-dependent; projection; finite-outcomes; release-gated; not-proof-storage; not-policy-engine; not-release-approval
tags: [kfm, contracts, ui, citation-validation-report, CitationValidationReport, evidence, citation, EvidenceDrawerPayload, EvidenceBundle, EvidenceRef, PolicyDecision, RuntimeResponseEnvelope, ReleaseManifest, accessibility]
related:
  - ./README.md
  - ./evidence_drawer_payload.md
  - ./evidence_drawer_payload/README.md
  - ../evidence/citation_validation_report.md
  - ../evidence/evidence_drawer_payload.md
  - ../evidence/evidence_bundle.md
  - ../evidence/evidence_ref.md
  - ../runtime/runtime_response_envelope.md
  - ../runtime/decision_envelope.md
  - ../policy/policy_decision.md
  - ../release/release_manifest.md
  - ../../schemas/contracts/v1/ui/citation_validation_report.schema.json
  - ../../schemas/contracts/v1/evidence/citation_validation_report.schema.json
  - ../../policy/ui/
  - ../../policy/evidence/
  - ../../policy/runtime/
  - ../../fixtures/ui/citation_validation_report/
  - ../../tools/validators/ui/validate_citation_validation_report.py
  - ../../docs/architecture/ui/README.md
  - ../../docs/architecture/ui/EVIDENCE_DRAWER.md
notes:
  - "Expanded from a PROPOSED greenfield scaffold at `contracts/ui/citation_validation_report.md`."
  - "A paired UI schema stub exists at `schemas/contracts/v1/ui/citation_validation_report.schema.json`; it requires only `id`, allows additional properties, and names this contract doc."
  - "A stronger evidence-family semantic contract exists at `contracts/evidence/citation_validation_report.md`; this UI-family contract is a UI projection/profile and must not duplicate evidence authority."
  - "UI contracts are semantic meaning only; UI code, schemas, policy, fixtures, tests, validators, runtime routes, release artifacts, and proof stores remain in separate roots."
  - "Rollback target for this expansion is previous scaffold blob SHA `1855a237089e22baa1208441ed5e17f70389940d`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI CitationValidationReport Contract

> `CitationValidationReport` in the UI family is the presentation-safe profile of citation/source-support checking results that a UI may render in the Evidence Drawer, Focus Mode, exports, diagnostics, or review-facing trust surfaces. It is downstream of evidence validation and policy filtering. It is not EvidenceBundle closure, not a PolicyDecision, not release approval, not proof storage, and not AI answer authority.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts/ui" src="https://img.shields.io/badge/root-contracts%2Fui-blue">
  <img alt="Object: CitationValidationReport" src="https://img.shields.io/badge/object-CitationValidationReport-purple">
  <img alt="Schema: stub confirmed" src="https://img.shields.io/badge/schema-stub__confirmed-orange">
  <img alt="Boundary: projection not authority" src="https://img.shields.io/badge/boundary-projection__not__authority-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/ui/citation_validation_report.md`  
**Paired UI schema:** `schemas/contracts/v1/ui/citation_validation_report.schema.json`  
**Schema posture:** PROPOSED stub; required field `id` only; `additionalProperties: true`  
**Evidence-family semantic contract:** `contracts/evidence/citation_validation_report.md`  
**Owning root:** `contracts/ui/` — UI-facing semantic meaning only  
**Truth posture:** CONFIRMED target was a greenfield scaffold · CONFIRMED paired UI schema stub exists and names this contract doc · CONFIRMED evidence-family CitationValidationReport contract exists and defines stronger report meaning/boundaries · CONFIRMED UI README says UI contracts are semantic meaning only and not implementation · NEEDS VERIFICATION for final canonical home, UI/evidence split, schema expansion, fixtures, validators, policy wiring, runtime/API behavior, and UI rendering

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Authority split](#authority-split) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [UI projection rules](#ui-projection-rules) · [Recommended UI fields](#recommended-ui-fields) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This contract defines how citation validation results may be carried to UI trust surfaces.

It answers:

- what citation validation status means when shown in UI;
- what negative states the UI must preserve;
- which evidence, citation, source, policy, review, release, and remediation references must remain visible when material;
- how UI should treat unresolved, stale, blocked, missing, denied, or unverified citation support;
- what the UI must not infer from a report.

It does not answer:

- whether a claim is true;
- whether an EvidenceBundle is closed;
- whether policy permits public display;
- whether release is approved;
- whether proof records exist;
- whether AI text is correct;
- whether a validator actually ran.

---

## Meaning

A UI `CitationValidationReport` is a trust-surface projection of citation/source-support checking.

A mature governed flow should look like:

```text
claim / layer / drawer payload / focus answer / export candidate
  -> evidence citation validation
  -> policy and sensitivity filtering
  -> review / release gate consideration
  -> UI CitationValidationReport projection
  -> UI renders PASS / WARN / FAIL / HOLD / DENY / ABSTAIN / ERROR / NEEDS_VERIFICATION safely
```

The UI report must preserve the validation outcome and limitations. It must never hide a failure by rendering the claim as fully supported.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| UI report meaning | `contracts/ui/citation_validation_report.md` | This file; UI-facing projection/profile only. |
| Evidence-family report meaning | `contracts/evidence/citation_validation_report.md` | Stronger evidence-family citation report semantics. |
| Evidence closure | `contracts/evidence/evidence_bundle.md` | EvidenceBundle closes claim support; report does not. |
| Evidence pointer | `contracts/evidence/evidence_ref.md` | EvidenceRef points to evidence; report checks/mentions it. |
| UI payload display | `contracts/ui/evidence_drawer_payload.md` and related UI contracts | Drawer/focus/export surfaces consume report state. |
| Runtime finite outcome | `contracts/runtime/runtime_response_envelope.md`, `contracts/runtime/decision_envelope.md` | Runtime/API owns outcome envelopes. |
| Policy/admissibility | `policy/ui/`, `policy/evidence/`, `policy/runtime/`, sensitivity/rights/release policy roots | Policy owns display decisions. |
| Machine shape | `schemas/contracts/v1/ui/citation_validation_report.schema.json` | Current stub only; field realization remains proposed. |
| Fixtures/tests/validators | `fixtures/ui/citation_validation_report/`, `tools/validators/ui/`, `tests/` | Enforceability stays outside contracts. |
| Release/correction/rollback | `release/` and release contracts | Release state is separate. |

---

## Schema posture

The paired UI schema currently declares:

| Field | Required | Schema-confirmed shape | Meaning |
|---|---:|---|---|
| `id` | yes | string | Canonical identifier for this UI report/projection. |
| `version` | no | string | Contract or object version. |
| `spec_hash` | no | string | Deterministic content/spec hash. |

The schema also confirms:

```text
additionalProperties: true
```

Because the schema is permissive, most fields in this contract are PROPOSED semantic guidance until schemas, fixtures, validators, policy tests, and UI/runtime behavior are verified.

---

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Showing citation validation status in an Evidence Drawer | Yes | Must render negative states visibly. |
| Showing why a claim is abstained, denied, held, or failed | Yes | Must avoid leaking restricted details. |
| Supporting Focus Mode or AI answer trust display | Conditional | Must remain downstream of EvidenceBundle, policy, and runtime outcome. |
| Supporting export/share diagnostics | Conditional | Exported UI must preserve caveats, citation state, and release posture. |
| Treating PASS as publication approval | No | ReleaseManifest/review/policy remain separate. |
| Treating report as EvidenceBundle closure | No | EvidenceBundle owns closure. |
| Treating report as policy decision | No | PolicyDecision/policy roots own decisions. |
| Treating report as proof storage | No | Materialized proof belongs in proof/data roots. |

---

## Exclusions

This contract must not be used as:

| Misuse | Required home/outcome |
|---|---|
| EvidenceBundle closure | Use EvidenceBundle. |
| PolicyDecision | Use policy/runtime/evidence policy outputs. |
| ReleaseManifest or publication approval | Use release roots. |
| Validator implementation | Use tools/tests/CI. |
| UI component implementation | Use UI/web/app roots. |
| Raw proof, citation payload, or source record storage | Use governed evidence/source/proof/data roots. |
| Direct model answer authority | Use governed AI/runtime/evidence flow with cite-or-abstain. |
| Browser access to canonical/proof/source stores | Deny; use governed API projections. |

---

## UI projection rules

PROPOSED UI rules:

- UI must preserve validation outcomes and reason codes in user-visible or steward-visible form appropriate to the audience.
- UI must distinguish missing citations, unresolved EvidenceRefs, failed EvidenceBundle closure, stale source, rights block, sensitivity block, redaction, review hold, release hold, and validator error.
- UI must not convert `FAIL`, `DENY`, `HOLD`, `ABSTAIN`, `ERROR`, or `NEEDS_VERIFICATION` into a normal supported claim.
- UI must show public-safe caveats without leaking restricted fields or exact sensitive values.
- UI must keep accessibility labels aligned with the trust state.
- UI must not read raw proof/source/internal stores to complete a missing report.
- UI must consume governed API/runtime projections and finite outcomes.

---

## Recommended UI fields

PROPOSED until schema expansion:

| Field | Meaning |
|---|---|
| `id` | UI report/projection identifier. |
| `version` | Object/contract version. |
| `spec_hash` | Baseline hash for deterministic report/rendering spec. |
| `checked_subject_ref` | Claim, drawer payload, map layer, focus answer, export, or API answer being checked. |
| `checked_subject_type` | Type of checked UI surface. |
| `outcome` | PASS, WARN, FAIL, HOLD, DENY, ABSTAIN, ERROR, or NEEDS_VERIFICATION. |
| `reason_codes` | Public-safe reason codes. |
| `display_summary` | Short public-safe summary. |
| `citation_count` | Count of citations checked. |
| `missing_count` | Count of missing expected citations. |
| `unresolved_count` | Count of unresolved refs/citations. |
| `blocked_count` | Count of rights/sensitivity/release-blocked citations. |
| `finding_refs` | Refs to full evidence-family findings, if allowed. |
| `evidence_bundle_refs` | EvidenceBundle refs shown or checked. |
| `policy_decision_ref` | Policy decision driving visible state. |
| `release_state_ref` | Release state or manifest reference. |
| `caveats` | Public-safe caveats/limitations. |
| `accessibility_label` | Trust-state label suitable for assistive tech. |
| `remediation_hint` | Public-safe next action or steward action, if allowed. |

---

## Validation expectations

NEEDS VERIFICATION:

- final canonical UI/evidence home split;
- schema expansion beyond `id`, `version`, and `spec_hash`;
- validator path and CI wiring;
- fixtures for PASS, WARN, FAIL, HOLD, DENY, ABSTAIN, ERROR, NEEDS_VERIFICATION;
- UI behavior in Evidence Drawer, Focus Mode, export/share, and diagnostics surfaces;
- policy filtering of sensitive citation details;
- accessibility-state tests;
- release-gate behavior when citation validation blocks public display.

---

## Open questions

- Should CitationValidationReport be canonical only under `contracts/evidence/`, with this UI file as a projection profile?
- Should the UI schema reference the evidence-family report schema or define a separate redacted projection schema?
- Which outcome vocabulary is final across UI, runtime, and evidence validation?
- Which details may public users see versus steward/internal users?
- Should UI reports be persisted or generated per governed API request only?

---

## Rollback

Rollback is required if this contract becomes evidence closure, policy authority, release approval, proof storage, validator implementation, UI component code, source truth, public API authority, or AI answer truth.

Rollback target for this expansion: previous scaffold blob SHA `1855a237089e22baa1208441ed5e17f70389940d`.

<p align="right"><a href="#top">Back to top</a></p>
