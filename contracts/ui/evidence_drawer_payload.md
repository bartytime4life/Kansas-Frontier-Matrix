<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-evidence-drawer-payload
title: contracts/ui/evidence_drawer_payload.md — UI EvidenceDrawerPayload Contract
type: semantic-contract; ui-projection-profile
version: v0.3
status: draft; PROPOSED; closed-schema-profile; fixture-first; bounded-executable; ui-family; evidence-drawer-projection; evidence-dependent; path-needs-review
owners: OWNER_TBD — UI steward · Evidence steward · Contracts steward · Schema steward · Policy steward · Release steward · Accessibility steward · Runtime steward · Docs steward
created: NEEDS VERIFICATION — greenfield scaffold existed before v0.2 expansion
updated: 2026-08-05
policy_label: public; contracts; ui; evidence-drawer-payload; EvidenceDrawerPayload; evidence-drawer; projection; finite-outcomes; correction-aware; negative-history; citation-capable; policy-filtered; release-gated; accessibility; no-sovereign-truth
tags: [kfm, contracts, ui, evidence-drawer-payload, EvidenceDrawerPayload, evidence-drawer, EvidenceBundle, EvidenceRef, CitationValidationReport, PolicyDecision, RuntimeResponseEnvelope, ReleaseManifest, RollbackCard, correction, supersession, accessibility, trust-badges]
related:
  - ./README.md
  - ./evidence_drawer_payload/README.md
  - ./citation_validation_report.md
  - ../evidence/evidence_drawer_payload.md
  - ../evidence/evidence_bundle.md
  - ../evidence/evidence_ref.md
  - ../evidence/citation_validation_report.md
  - ../runtime/runtime_response_envelope.md
  - ../runtime/decision_envelope.md
  - ../policy/policy_decision.md
  - ../release/release_manifest.md
  - ../../schemas/contracts/v1/ui/evidence_drawer_payload.schema.json
  - ../../schemas/contracts/v1/evidence/evidence_drawer_payload.schema.json
  - ../../policy/ui/
  - ../../policy/evidence/
  - ../../policy/runtime/
  - ../../fixtures/ui/evidence_drawer_payload/
  - ../../tools/validators/ui/validate_evidence_drawer_payload.py
  - ../../tests/validators/test_validate_evidence_drawer_payload.py
  - ../../apps/explorer-web/src/adapters/GovernedClient.ts
  - ../../apps/explorer-web/src/features/evidence_drawer/
  - ../../apps/explorer-web/tests/evidence-drawer.test.ts
  - ../../.github/workflows/evidence-drawer-payload.yml
  - ../../docs/architecture/ui/README.md
  - ../../docs/architecture/ui/EVIDENCE_DRAWER.md
notes:
  - "v0.2 expanded the prior greenfield scaffold while the paired UI schema remained permissive."
  - "v0.3 defines one closed, fixture-first public-safe UI projection profile already consumed by Explorer Web."
  - "Negative outcomes remain audit-visible only where the finite public projection permits them and always declare resolvable_as_current=false."
  - "Correction chains must be acyclic; every prior correction target is represented as superseded history and only a terminal target may support a current ANSWER."
  - "DENY and ERROR projections carry no evidence refs, citations, or history identifiers."
  - "The separate evidence-family contract/schema remain PATH-NEEDS-REVIEW; this change does not resolve or duplicate EvidenceBundle authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI EvidenceDrawerPayload Contract

> `EvidenceDrawerPayload` is the UI-facing governed projection that carries cited, policy-filtered evidence context to the Evidence Drawer. It makes finite trust state and bounded correction history visible; it does not create evidence, close an `EvidenceBundle`, execute policy, approve review or release, store proof, or authorize AI answers.

<p>
  <img alt="Status: proposed bounded profile" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts/ui" src="https://img.shields.io/badge/root-contracts%2Fui-blue">
  <img alt="Object: EvidenceDrawerPayload" src="https://img.shields.io/badge/object-EvidenceDrawerPayload-purple">
  <img alt="Schema: closed fixture-first profile" src="https://img.shields.io/badge/schema-closed__fixture--first-green">
  <img alt="Boundary: projection only" src="https://img.shields.io/badge/boundary-projection__only-critical">
</p>

**Status:** draft / PROPOSED / bounded executable profile  
**Path:** `contracts/ui/evidence_drawer_payload.md`  
**Object-folder guide:** `contracts/ui/evidence_drawer_payload/README.md`  
**Paired UI schema:** `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json`  
**Schema posture:** closed Draft 2020-12 profile; unknown fields denied; finite outcomes and bounded history represented  
**Profile:** `kfm.explorer.evidence-drawer.public-safe.v1`  
**Related evidence-family contract:** `contracts/evidence/evidence_drawer_payload.md` — still `PATH-NEEDS-REVIEW` for the final UI/evidence authority split  
**Truth posture:** CONFIRMED repository-owned schema, reusable synthetic fixtures, deterministic validator, Explorer parser/view-state implementation, unit/browser test surfaces, and read-only CI orchestration / PROPOSED public-safe profile semantics / NEEDS VERIFICATION for final canonical object-family home, live governed API transport, upstream policy and evidence authenticity, accountable review, release enforcement, correction-store resolution, deployment, and production accessibility

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Authority split](#authority-split) · [Machine profile](#machine-profile) · [Finite outcomes](#finite-outcomes) · [History and correction](#history-and-correction) · [Projection rules](#projection-rules) · [Validation](#validation) · [Non-effects](#non-effects) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This contract defines the UI-facing meaning of the bounded `EvidenceDrawerPayload` profile consumed by Explorer Web.

It answers:

- which finite outcome the drawer may render;
- which public-safe evidence references and citations may accompany an `ANSWER` or bounded `ABSTAIN`;
- which source-role, policy, review, release, freshness, and correction labels must remain visible;
- how held, denied, superseded, revoked, and withdrawn evidence may remain audit-visible without becoming current claim support;
- how a correction chain binds prior evidence to the active evidence reference; and
- what the browser must suppress for `DENY`, `ERROR`, malformed, or contradictory projections.

It does not decide whether a claim is true, whether an EvidenceBundle is authentic or complete, whether policy permits display, whether review authority exists, or whether a release is published.

---

## Meaning

`EvidenceDrawerPayload` is a governed projection envelope for the UI trust panel.

```text
clicked released feature / badge / consequential map claim
  -> governed claim-resolution request
  -> evidence + citation + policy + review + release checks
  -> RuntimeResponseEnvelope / DecisionEnvelope
  -> public-safe EvidenceDrawerPayload projection
  -> Explorer parser validates the bounded profile
  -> drawer renders ANSWER / ABSTAIN / DENY / ERROR
```

The payload renders what upstream governed systems declare. It does not resolve live evidence, recompute policy, authenticate review, perform release, or upgrade an abstention into an answer.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| UI-facing payload meaning | `contracts/ui/evidence_drawer_payload.md` | This bounded UI projection profile. |
| Evidence-facing payload meaning | `contracts/evidence/evidence_drawer_payload.md` | Existing adjacent contract; final home remains unresolved. |
| Evidence closure | `contracts/evidence/evidence_bundle.md` | `EvidenceBundle` remains canonical support. |
| Evidence pointer | `contracts/evidence/evidence_ref.md` | `EvidenceRef` is a governed pointer, not closure. |
| Runtime finite outcome | `contracts/runtime/runtime_response_envelope.md`, `contracts/runtime/decision_envelope.md` | Runtime/API owns upstream outcome semantics. |
| Policy/admissibility | `policy/ui/`, `policy/evidence/`, `policy/runtime/` | Policy owns allow, abstain, deny, and error decisions. |
| Machine shape | `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` | Closed shape for this UI profile only. |
| Reusable synthetic examples | `fixtures/ui/evidence_drawer_payload/` | Valid/invalid examples and expected findings. |
| Validation implementation | `tools/validators/ui/validate_evidence_drawer_payload.py` | Deterministic local declaration checks. |
| Browser projection | `apps/explorer-web/src/features/evidence_drawer/` | Rendering and accessibility; not evidence authority. |
| Release/correction/rollback | `release/` and their owning contracts/stores | Actual decisions and records remain separate. |

This profile does not settle the existing UI/evidence contract-home seam. It creates no third home and makes no evidence-family object authoritative.

---

## Machine profile

The paired schema is closed with `additionalProperties: false`. Required top-level fields are:

| Field | Meaning |
|---|---|
| `profile` | Exact profile identifier `kfm.explorer.evidence-drawer.public-safe.v1`. |
| `id` | Bounded canonical projection identifier. |
| `outcome` | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |
| `reason_code` | Stable public-safe reason code. |
| `title`, `summary` | Governed display text. Negative states are replaced by fixed browser copy. |
| `evidence_refs` | Bounded public-safe evidence identifiers permitted by the finite outcome. |
| `citations` | Bounded HTTPS citations permitted by the finite outcome. |
| `limitations` | Public-safe caveats. Negative states are not allowed to reflect them as claim text. |
| `trust_state` | Source role, policy, review, release, freshness, and correction state. |

Optional `history` contains only bounded identifiers and canonical UTC-second timestamps:

```text
history = {
  negative_outcomes: [
    {
      evidence_ref,
      state: HELD | DENIED | SUPERSEDED | REVOKED | WITHDRAWN,
      reason_code,
      recorded_at,
      visible_in_runtime: true,
      resolvable_as_current: false
    }
  ],
  corrections: [
    {
      prior_evidence_ref,
      active_evidence_ref,
      status: ACTIVE_CORRECTION,
      recorded_at
    }
  ]
}
```

Unknown fields, invalid HTTPS citations, control characters, oversized arrays, duplicate historical evidence identities, noncanonical timestamps, self-corrections, and correction cycles fail closed.

---

## Finite outcomes

| Outcome | Required state | Browser posture |
|---|---|---|
| `ANSWER` | `SUPPORTED`; nonempty evidence and citations; policy `ALLOW`; review `REVIEWED`; release `RELEASED`; freshness `CURRENT`. | Render governed title/summary, support, citations, limitations, trust labels, and safe history. |
| `ABSTAIN` | Non-supported reason; policy `ABSTAIN`. | Render fixed reason copy; may retain safe evidence refs and bounded history where the reason permits it. |
| `DENY` | Non-supported reason; policy `DENY`; no evidence refs, citations, or history. | Render fixed no-leak copy only. |
| `ERROR` | `UPSTREAM_ERROR`; policy `ERROR`; no evidence refs, citations, or history. | Render fixed error copy only; never fall back to an answer. |

`SUPPORTED` is valid only for `ANSWER`. A malformed or internally contradictory payload becomes the app-local `INVALID_PAYLOAD` error state and no input values are reflected.

---

## History and correction

Negative evidence remains visible only as a bounded audit state. It cannot resolve as current support.

Rules:

1. Every negative record has `visible_in_runtime: true` and `resolvable_as_current: false`.
2. Its state and reason code must agree: held, denied, superseded, revoked, or withdrawn.
3. A negative evidence ref must not also appear in current `evidence_refs`.
4. `DENY` and `ERROR` expose no history identifiers.
5. `SUPERSEDED_EVIDENCE`, `HELD_EVIDENCE`, `WITHDRAWN_EVIDENCE`, and `REVOKED_EVIDENCE` abstentions require a matching negative-history record.
6. Correction edges must be acyclic, non-self-referential, and unique by prior ref.
7. Every correction prior ref must be represented as `SUPERSEDED` negative history.
8. Only terminal correction targets may be current answer support; every terminal target must appear in `evidence_refs`.
9. Intermediate correction targets remain superseded history and never become simultaneous current support.

This is declaration validation only. The profile does not dereference a correction registry, authenticate a notice, prove timestamps, or establish that a public cache was invalidated.

---

## Projection rules

- The payload must come from governed API/runtime code after evidence, policy, citation, review, and release checks.
- The drawer must preserve finite negative states and never convert missing, stale, denied, held, superseded, revoked, or withdrawn evidence into an `ANSWER`.
- Current evidence and audit history remain separate fields and identities.
- Denial and error details are fixed in the browser; untrusted title, summary, limitation, evidence, citation, and history values are suppressed.
- The browser must not read RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, canonical stores, proof stores, or direct model output.
- Accessibility labels and visible trust labels must describe the same finite state.
- A schema-valid payload remains a projection candidate; it is not evidence, policy, review, release, correction, rollback, or publication proof.

---

## Validation

### Confirmed bounded checks

```bash
python tools/validators/ui/validate_evidence_drawer_payload.py --fixtures
python -m unittest -q tests.validators.test_validate_evidence_drawer_payload
pnpm --filter explorer-web build
pnpm --filter explorer-web test
```

The dedicated validator checks:

- Draft 2020-12 schema validity and closed shape;
- exact positive/negative fixture polarity;
- finite outcome/trust-state consistency;
- no current/negative evidence overlap;
- correction-chain acyclicity and terminal binding;
- state/reason consistency;
- denial/error no-leak declarations;
- bounded JSON parsing, duplicate keys, non-finite numbers, and no-network behavior.

Explorer tests independently check parser parity, fixed no-leak copy, safe history rendering, keyboard open/close, focus entry/return, and browser DOM suppression for denied/error states.

### Still needs verification

- final canonical UI/evidence home split;
- live governed API transport and schema negotiation;
- evidence, policy, review, release, correction, and rollback authenticity;
- source rights and sensitive-field filtering upstream;
- map-click, Focus Mode, export/share, diagnostics, and telemetry integration;
- production accessibility, focus trapping, reduced motion, and non-map alternatives;
- cache invalidation and correction propagation across released public surfaces;
- required-check and branch-protection enforcement.

---

## Non-effects

A passing schema, fixture, validator, TypeScript build, unit test, browser test, workflow, or authoring receipt does not:

- resolve or authenticate an `EvidenceRef` or `EvidenceBundle`;
- decide rights, sensitivity, policy, review authority, or release state;
- create a `CorrectionNotice`, `RollbackCard`, `ReleaseManifest`, or public claim;
- publish, deploy, promote, invalidate a cache, or authorize public use; or
- make the UI/evidence contract-home seam resolved.

---

## Open questions

- Should the long-term canonical semantic contract remain under `contracts/ui/`, move to `contracts/evidence/`, or preserve a documented UI-projection/evidence-object split?
- Should a later profile add explicit bundle, policy-decision, review, release-manifest, correction-notice, and rollback references after their canonical schemas are ratified?
- Which source and citation details may public users see versus steward/internal users?
- Should projections be generated per request, cached by release/spec hash, or persisted as release-bound artifacts?
- Which upstream service guarantees correction-chain completeness and public-cache invalidation?

---

## Rollback

Before merge, close the draft pull request and delete only its feature branch. After merge, revert the implementation commit through a reviewed pull request. Reversion restores the prior permissive schema and view-state behavior; it performs no lifecycle data migration, source change, public release, or external-system cleanup.

<p align="right"><a href="#top">Back to top</a></p>
