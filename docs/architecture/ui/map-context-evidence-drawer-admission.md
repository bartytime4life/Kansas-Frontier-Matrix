<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://architecture/ui/map-context-evidence-drawer-admission
title: MapContextEnvelope to EvidenceDrawerPayload Admission Boundary
type: architecture; ui-runtime-boundary; anticorruption-adapter; fixture-first
version: v0.1.0
status: proposed; implemented-helper; no-network; no-authority
owners: OWNER_TBD — UI steward · Runtime steward · Evidence steward · Validation steward
created: 2026-08-07
updated: 2026-08-07
policy_label: public; ui; runtime; evidence-drawer; renderer-neutral; public-safe
related:
  - ../../../contracts/ui/map_context_envelope.md
  - ../../../contracts/ui/evidence_drawer_payload.md
  - ../../../contracts/runtime/decision_envelope.md
  - ../../../schemas/contracts/v1/ui/map_context_envelope.schema.json
  - ../../../schemas/contracts/v1/ui/evidence_drawer_payload.schema.json
  - ../../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../../packages/envelopes/src/envelopes/map_context_evidence_drawer.py
  - ../../../tools/validators/ui/validate_map_context_evidence_drawer_admission.py
  - ../../../fixtures/ui/map_context_evidence_drawer_admission/
  - ../../../tests/packages/envelopes/test_map_context_evidence_drawer_admission.py
[/KFM_META_BLOCK_V2] -->

# Map context to Evidence Drawer admission

> A deterministic anticorruption adapter that checks whether an existing
> renderer-neutral `MapContextEnvelope` and an existing public-safe
> `EvidenceDrawerPayload` remain aligned for one selected feature, then emits an
> existing `DecisionEnvelope` **candidate**. It creates no evidence, policy,
> review, release, publication, or public-use authority.

## Why this boundary exists

The map shell knows which released layer and feature the user selected. The
Evidence Drawer knows the finite public-safe projection the governed runtime
intends to display. Neither object should absorb the other's model, and neither
should pass MapLibre-native state, raw feature properties, canonical-store
handles, or unreviewed evidence across the trust membrane.

The adapter therefore acts as a published-language boundary:

```text
released map state
  -> validated MapContextEnvelope
  -> validated EvidenceDrawerPayload
  -> cross-object admission adapter
  -> DecisionEnvelope candidate
  -> governed runtime / policy / evidence handling
```

The adapter does not replace either source validator. Callers must validate the
two input objects first.

## Inputs and output

| Surface | Role |
|---|---|
| `MapContextEnvelope` | Carries renderer-neutral layer, selection, time, area, evidence, and release context. |
| `EvidenceDrawerPayload` | Carries a finite, public-safe UI projection with trust state and citations. |
| Adapter parameters | Supply a deterministic decision ID, evaluation time, and an explicit fixture-only opt-in for `SYSTEM_TEST`. |
| `DecisionEnvelope` candidate | Carries the finite render-admission posture without copying title, summary, citation URLs, limitations, history, renderer state, or raw properties. |

No new schema or authority object is introduced. The output uses the existing
`DecisionEnvelope` shape and `policy_family = "render"`.

## Admission checks

The adapter checks only explicit local relationships:

1. Both objects use the expected existing profiles.
2. Evaluation occurs after context assembly and no later than context expiry.
3. Every `MapContextEnvelope.governance` declaration remains `false`.
4. `SYSTEM_TEST` is denied unless the caller explicitly enables fixture-only use.
5. Exactly one selected feature is present; zero or multiple selections abstain.
6. The selected layer resolves exactly once, is declared `PUBLISHED`, and its
   release reference belongs to the context release set.
7. Selected evidence belongs to the context evidence set.
8. `ANSWER` and `ABSTAIN` drawer evidence is a subset of the selected feature's
   evidence, not merely any visible layer evidence.
9. Drawer outcome, reason, citations, and trust-state declarations are internally
   compatible with `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.
10. `DENY` and `ERROR` never copy evidence, citations, history, or source text into
    the emitted candidate.

These checks validate declarations and relationships only. They do not verify
that a release reference resolves, that evidence exists, that policy was
correctly evaluated, or that review is authentic.

## Finite outcomes

| Outcome | Typical adapter reason | Meaning |
|---|---|---|
| `ANSWER` | `SUPPORTED` | The validated drawer support is selected-feature-scoped and its declared trust state is answer-compatible. |
| `ABSTAIN` | `STALE_EVIDENCE`, `CONTEXT_EXPIRED`, `SELECTION_REQUIRED`, `SELECTION_AMBIGUOUS` | The adapter cannot safely admit a current answer. |
| `DENY` | `SENSITIVE_DETAIL_RESTRICTED`, `CALLER_ROLE_DENIED` | The declared public projection or caller role is denied without support leakage. |
| `ERROR` | `UPSTREAM_ERROR`, `DRAWER_EVIDENCE_OUTSIDE_SELECTION`, `DRAWER_TRUST_STATE_MISMATCH` | Input declarations are inconsistent or an upstream safe error must propagate. |

## Non-effects

A successful adapter call does **not**:

- resolve `EvidenceRef` to `EvidenceBundle`;
- evaluate rights, sensitivity, access, consent, or render policy;
- authenticate a caller, reviewer, steward, signer, or release;
- authorize a capability, public use, export, Focus Mode response, or publication;
- read RAW, WORK, QUARANTINE, canonical, proof, or model stores;
- mutate repository, runtime, map, catalog, lifecycle, or release state;
- prove that the Explorer UI or governed API invokes the helper.

## Directory Rules basis

| Responsibility | Home |
|---|---|
| Shared side-effect-minimal adapter code | `packages/envelopes/src/envelopes/` |
| Architecture explanation | `docs/architecture/ui/` |
| Synthetic cross-object examples | `fixtures/ui/` |
| Operational fixture replay | `tools/validators/ui/` |
| Package behavior tests | `tests/packages/envelopes/` |
| Read-only hosted validation | `.github/workflows/` |
| AI authoring provenance | `data/receipts/generated/` |

The placement uses existing responsibility roots. It creates no new root and no
parallel contract, schema, policy, evidence, release, proof, receipt, or
publication home.

## Validation

The focused packet must prove:

- exact eight-case finite outcomes;
- current `DecisionEnvelope` schema conformance for every emitted candidate;
- deterministic replay and input immutability;
- no title, summary, citation URL, limitation, history, or canary leakage;
- no-network execution;
- source fixture validation through the existing MapContext and Evidence Drawer
  validators;
- generated authoring-receipt integrity.

## Rollback

Before merge, close the draft pull request and delete its feature branch. After
an authorized merge, revert the bounded adapter packet. No data migration,
source deactivation, reprocessing, release withdrawal, cache invalidation, or
public correction is required because this helper does not activate a runtime
route or change published state.
