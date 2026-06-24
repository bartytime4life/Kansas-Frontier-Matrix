<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-map-context-envelope-readme
title: contracts/ui/map_context_envelope — MapContextEnvelope UI Object Folder README
type: readme
version: v0.1
status: draft; PROPOSED; object-folder-readme; map-ui-envelope; focus-mode-admission; path-needs-review; schema-missing-in-session
owners: OWNER_TBD — UI steward · Map steward · Focus Mode steward · Runtime steward · Contracts steward · Schema steward · Policy steward · Release steward · Docs steward
created: 2026-06-24
updated: 2026-06-24
policy_label: public; contracts; ui; map-context-envelope; focus-mode; maplibre; admission-check; immutable-envelope; release-gated; evidence-dependent; no-direct-store-access
tags: [kfm, contracts, ui, map-context-envelope, MapContextEnvelope, maplibre, focus-mode, viewport, layer-ids, feature-ids, release-refs, evidence-refs, spec-hash, admission-check, trust-membrane]
related:
  - ../README.md
  - ../../../docs/focus-mode/state/map-context-state.md
  - ../../../docs/focus-mode/state/payload-state.md
  - ../../../docs/focus-mode/state/finite-outcomes.md
  - ../../../docs/architecture/ui/FOCUS_FLOW.md
  - ../../../docs/architecture/ui/MAP_RUNTIME_BOUNDARY.md
  - ../../../docs/architecture/ui/EVIDENCE_DRAWER.md
  - ../../../contracts/focus_mode/focus_mode_payload.md
  - ../../../contracts/runtime/runtime_response_envelope.md
  - ../../../contracts/runtime/decision_envelope.md
  - ../../../contracts/evidence/evidence_ref.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../contracts/release/release_manifest.md
  - ../../../schemas/contracts/v1/focus_mode/map_context_envelope.schema.json
  - ../../../schemas/contracts/v1/ui/map_context_envelope.schema.json
  - ../../../policy/runtime/
  - ../../../policy/focus/
  - ../../../policy/release/
notes:
  - "This file replaces a blank placeholder at `contracts/ui/map_context_envelope/README.md`."
  - "Current session evidence did not verify a flat `contracts/ui/map_context_envelope.md`, `contracts/focus_mode/map_context_envelope.md`, or paired schema file."
  - "`docs/focus-mode/state/map-context-state.md` defines the doctrine and proposed shape/freshness/admission rules for MapContextEnvelope and notes path placement divergence."
  - "This README is an object-folder guide and guard only; it is not the runtime implementation, not schema enforcement, not map state storage, not evidence closure, not release approval, and not a browser bypass."
  - "Rollback target for this replacement is previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/ui/map_context_envelope

> Proposed object-folder README for `MapContextEnvelope`, the bounded, immutable map-state snapshot that a UI or Focus Mode surface may submit to a governed runtime. The envelope carries map context for admission and resolution; it must not become live map state storage, raw layer access, evidence truth, release approval, or direct browser access to canonical stores.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Object: MapContextEnvelope" src="https://img.shields.io/badge/object-MapContextEnvelope-blueviolet">
  <img alt="Boundary: immutable envelope" src="https://img.shields.io/badge/boundary-immutable__envelope-critical">
  <img alt="Admission: required" src="https://img.shields.io/badge/admission-required-0a7ea4">
  <img alt="Schema: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
</p>

**Status:** draft / PROPOSED object-folder README  
**Path:** `contracts/ui/map_context_envelope/README.md`  
**Current evidence anchor:** `docs/focus-mode/state/map-context-state.md`  
**Flat contract path:** `contracts/ui/map_context_envelope.md` — not verified in this session  
**Focus Mode contract path:** `contracts/focus_mode/map_context_envelope.md` — not verified in this session  
**Schema home:** `schemas/contracts/v1/focus_mode/map_context_envelope.schema.json` or `schemas/contracts/v1/ui/map_context_envelope.schema.json` — NEEDS VERIFICATION  
**Truth posture:** CONFIRMED placeholder was blank · CONFIRMED MapContextEnvelope doctrine exists in Focus Mode state docs · CONFIRMED doctrine describes an immutable envelope consumed by runtime and not direct map reads · NEEDS VERIFICATION for canonical contract path, schema path, validator, fixtures, runtime implementation, UI implementation, policy gates, release refs, and persisted receipts

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Authority split](#authority-split) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Admission rules](#admission-rules) · [Validation checklist](#validation-checklist) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This folder exists to hold or document the UI-facing `MapContextEnvelope` object family if KFM accepts an object-folder layout under `contracts/ui/`.

A `MapContextEnvelope` should describe the map context that a governed runtime may admit before answering, focusing, resolving evidence, or assembling downstream payloads.

It may include or point to:

- time window;
- visible or selected layer ids;
- selected feature ids;
- layer/style/filter `spec_hash`;
- release refs;
- evidence refs;
- area scope;
- assembled timestamp;
- spec version;
- request id;
- caller role;
- optional viewport-pull descriptors where policy permits.

This folder must not become canonical runtime behavior or map state storage without an accepted contract/schema/ADR decision.

---

## Meaning

`MapContextEnvelope` is a request-context envelope, not a claim, not an answer, and not evidence closure.

A mature governed flow should look like:

```text
Map UI state
  -> MapContextEnvelope assembly
  -> schema / version / freshness / release / feature / role admission
  -> runtime accepts or returns ERROR / DENY
  -> evidence and policy resolution
  -> FocusModePayload / EvidenceDrawerPayload / RuntimeResponseEnvelope
```

The runtime should read the envelope, not the live browser map store. If the envelope is stale, malformed, missing release refs, bound to non-PUBLISHED layers, or inconsistent with feature/layer membership, the runtime should reject it rather than guessing.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| Object-folder boundary | `contracts/ui/map_context_envelope/README.md` | This README; guide/guard only. |
| Semantic contract | `contracts/ui/map_context_envelope.md` or `contracts/focus_mode/map_context_envelope.md` after steward decision | Not verified in this session. |
| Focus Mode doctrine | `docs/focus-mode/state/map-context-state.md` | Current verified doctrine anchor. |
| Machine shape | `schemas/contracts/v1/focus_mode/` or `schemas/contracts/v1/ui/` after ADR/steward decision | Schema path not verified in this session. |
| Runtime response | `contracts/runtime/runtime_response_envelope.md` | Runtime emits finite outcome response. |
| Decision/admission state | `contracts/runtime/decision_envelope.md`, policy roots | Runtime/policy decide; envelope carries input state. |
| Evidence refs | `contracts/evidence/evidence_ref.md`, `contracts/evidence/evidence_bundle.md` | Evidence resolution stays upstream/governed. |
| Release refs | `contracts/release/release_manifest.md`, release roots | Release state is separate and must be inspectable. |
| UI implementation | UI/web/app roots | Component/state code stays outside contracts. |
| Fixtures/tests/validators | `fixtures/`, `tests/`, `tools/validators/` | Enforceability stays outside contracts. |

---

## Accepted contents

Only object-folder support material belongs here:

| Accepted item | Purpose |
|---|---|
| `README.md` | Defines folder boundary and points to doctrine/contract/schema homes. |
| `MIGRATION.md` | Optional plan if UI/focus-mode contract homes are consolidated. |
| `BACKLINKS.md` | Optional stale-reference audit. |
| `ADR_POINTER.md` | Optional pointer to accepted path/schema/home decision. |

No field semantics should be maintained here if a flat contract file becomes canonical.

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| Browser state stores | UI/web/app roots | Contracts do not store live UI state. |
| Raw layer data or tiles | map/data/release roots | Envelope carries refs, not source data. |
| EvidenceBundle records | evidence/data proof roots | Envelope may carry EvidenceRefs, not evidence closure. |
| JSON Schema | `schemas/contracts/v1/...` | Schemas own shape. |
| Policy rules | `policy/` roots | Policy owns admission/deny/restrict behavior. |
| Runtime implementation | runtime/API roots | Contracts do not implement admission. |
| Fixtures/tests/validators | `fixtures/`, `tests/`, `tools/validators/` | Proof and enforcement stay outside contracts. |
| Release manifests or rollback cards | `release/` and release contracts | Release state remains separate. |
| AI answer text or model state | governed AI/runtime roots | AI output is downstream and receipt-bound. |

---

## Admission rules

PROPOSED semantic rules, derived from current doctrine evidence:

- The envelope must be immutable after assembly.
- The runtime must admit or reject the envelope before evidence/payload work begins.
- Failing admission is `ERROR` or `DENY`, not best-effort answering.
- Visible `layer_ids` must resolve to released/PUBLISHED layer state.
- `feature_ids` must belong to the cited layers.
- `release_refs` must resolve.
- `spec_hash` must match or be explicitly rebound with a receipt/caveat.
- `assembled_at` must be fresh enough for admission.
- `caller_role` must be policy-admitted for the surface.
- `evidence_refs` must resolve or lead to governed `ABSTAIN`/`ERROR` handling.
- The envelope must not carry query text if the accepted request model keeps query separate.

---

## Validation checklist

- [ ] Resolve canonical semantic contract path: UI, Focus Mode, or split.
- [ ] Verify schema file and field set.
- [ ] Verify validator exists and checks freshness, layer/release binding, feature membership, caller role, and spec version.
- [ ] Verify fixture coverage for current, stale, rebindable, malformed, non-PUBLISHED layer, dangling release ref, missing evidence ref, unsupported spec version, and caller-role deny.
- [ ] Verify UI implementation assembles envelopes from released/governed map state only.
- [ ] Verify runtime does not read live UI store, raw layer data, canonical/internal stores, or direct model state.
- [ ] Verify any rebind emits a receipt and preserves auditability.

---

## Open questions

- Should `MapContextEnvelope` live under `contracts/ui/`, `contracts/focus_mode/`, or both with split responsibilities?
- Should the schema home be `schemas/contracts/v1/ui/` or `schemas/contracts/v1/focus_mode/`?
- Which object owns viewport-pull governance: this envelope, FocusModeRequest, map runtime, or a separate contract?
- Should query text always remain outside the envelope?
- What TTL and freshness states are accepted for public versus steward/internal callers?

---

## Rollback

Rollback is required if this folder becomes live map state storage, schema authority, policy authority, runtime implementation, EvidenceBundle closure, release approval, raw/canonical-store access, UI bypass, or AI answer authority.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
