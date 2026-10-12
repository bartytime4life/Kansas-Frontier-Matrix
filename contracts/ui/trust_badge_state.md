<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-trust-badge-state
title: contracts/ui/trust_badge_state.md — UI TrustBadgeState Contract
type: semantic-contract
version: v0.2
status: draft; PROPOSED; schema-stub-confirmed; ui-family; trust-visible-state; evidence-dependent; release-gated
owners: OWNER_TBD — UI steward · Evidence steward · Runtime steward · Policy steward · Release steward · Schema steward · Accessibility steward · Docs steward
created: NEEDS VERIFICATION — greenfield scaffold existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; ui; trust-badge-state; trust-visible-state; projection; evidence-dependent; release-gated; accessibility; no-sovereign-truth
tags: [kfm, contracts, ui, trust-badge-state, TrustBadgeState, trust-badges, EvidenceDrawerPayload, EvidenceBundle, EvidenceRef, CitationValidationReport, PolicyDecision, ReleaseManifest, accessibility]
related:
  - ./README.md
  - ./evidence_drawer_payload.md
  - ./citation_validation_report.md
  - ./story_manifest.md
  - ./story_node.md
  - ../evidence/evidence_bundle.md
  - ../evidence/evidence_ref.md
  - ../evidence/citation_validation_report.md
  - ../runtime/runtime_response_envelope.md
  - ../policy/policy_decision.md
  - ../release/release_manifest.md
  - ../../schemas/contracts/v1/ui/trust_badge_state.schema.json
  - ../../policy/ui/
  - ../../fixtures/ui/trust_badge_state/
  - ../../docs/architecture/ui/TRUST_BADGES.md
  - ../../docs/brand/trust-state-visuals.md
notes:
  - "Expanded from a PROPOSED greenfield scaffold at `contracts/ui/trust_badge_state.md`."
  - "A paired UI schema stub exists at `schemas/contracts/v1/ui/trust_badge_state.schema.json`; it requires only `id`, allows additional properties, and names this contract doc."
  - "UI trust-badge architecture says badges expose trust state, not evidence; they route to proof and never stand in for it."
  - "This contract defines UI-facing badge state meaning only. It is not evidence, policy, release, proof storage, or UI implementation."
  - "Rollback target for this expansion is previous scaffold blob SHA `5e92d12755ca7db74a77293e9880d0abb0c5c6a4`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI TrustBadgeState Contract

> `TrustBadgeState` is the UI-facing state object for trust-visible badges across KFM surfaces. A badge exposes trust posture and routes users toward evidence or policy context. It is not evidence, not proof, not release approval, not policy execution, and not a substitute for the Evidence Drawer.

<p>
  <img alt="Status: PROPOSED" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Family: UI" src="https://img.shields.io/badge/family-ui-0a7ea4">
  <img alt="Object: TrustBadgeState" src="https://img.shields.io/badge/object-TrustBadgeState-purple">
  <img alt="Schema: stub confirmed" src="https://img.shields.io/badge/schema-stub__confirmed-orange">
  <img alt="Boundary: badge not proof" src="https://img.shields.io/badge/boundary-badge__not__proof-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/ui/trust_badge_state.md`  
**Paired schema:** `schemas/contracts/v1/ui/trust_badge_state.schema.json`  
**Schema posture:** PROPOSED stub; required field `id` only; `additionalProperties: true`  
**Architecture anchor:** `docs/architecture/ui/TRUST_BADGES.md`  
**Truth posture:** CONFIRMED target was a greenfield scaffold · CONFIRMED paired UI schema stub exists and names this contract doc · CONFIRMED trust badge architecture defines badges as trust state, not evidence · NEEDS VERIFICATION for final schema, fixtures, validator, UI implementation, policy wiring, and release behavior

**Quick jumps:** [Purpose](#purpose) · [Repo fit](#repo-fit) · [Meaning](#meaning) · [Authority split](#authority-split) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Finite states](#finite-states) · [Recommended UI fields](#recommended-ui-fields) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This contract defines how UI trust badges communicate trust posture without pretending to be the underlying proof.

It answers:

- which trust state a badge may show;
- what evidence, policy, release, freshness, review, correction, or citation context the badge points toward;
- what the UI must preserve for accessibility and non-color interpretation;
- how badge state should remain distinct from evidence, policy, release, and proof objects.

It does not answer whether a claim is true, whether a release is approved, whether evidence is complete, or whether UI code is implemented.

## Repo fit

| Relationship | Path | Status |
|---|---|---|
| This semantic contract | `contracts/ui/trust_badge_state.md` | PROPOSED / current file |
| Trust badge architecture | `docs/architecture/ui/TRUST_BADGES.md` | CONFIRMED doctrine/architecture anchor |
| Paired UI schema | `schemas/contracts/v1/ui/trust_badge_state.schema.json` | CONFIRMED permissive stub |
| Evidence Drawer payload | `contracts/ui/evidence_drawer_payload.md` | Related UI payload surface |
| Citation validation | `contracts/ui/citation_validation_report.md` | Related UI validation projection |
| UI policy home | `policy/ui/` | Referenced by schema; implementation depth NEEDS VERIFICATION |
| UI fixtures | `fixtures/ui/trust_badge_state/` | Referenced by schema; existence/coverage NEEDS VERIFICATION |

## Meaning

A `TrustBadgeState` is a compact, accessible UI projection of trust posture.

```text
Evidence / policy / release / freshness / review / correction state
  -> governed UI payload
  -> TrustBadgeState
  -> badge display
  -> click or inspect path to Evidence Drawer / safe detail surface
```

A badge may summarize. It must not replace the detail surface or the upstream evidence and policy objects.

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| UI badge state meaning | `contracts/ui/trust_badge_state.md` | This file. |
| Badge architecture | `docs/architecture/ui/TRUST_BADGES.md` | Human-facing UI doctrine. |
| Evidence support | `contracts/evidence/` | EvidenceBundle and EvidenceRef support claims. |
| Citation checking | `contracts/evidence/citation_validation_report.md` and `contracts/ui/citation_validation_report.md` | Citation validation remains separate. |
| Policy/admissibility | `policy/ui/`, `policy/evidence/`, `policy/runtime/` | Policy owns allow/restrict/abstain decisions. |
| Release state | `contracts/release/` and release roots | Release state remains separate. |
| Machine shape | `schemas/contracts/v1/ui/trust_badge_state.schema.json` | Current stub only. |
| UI rendering | UI/web/app roots | Badge component code stays outside contracts. |
| Visual design tokens | docs/brand or design/style roots | Colors/icons must not become policy truth. |

## Schema posture

The paired UI schema currently confirms:

| Field | Required | Shape |
|---|---:|---|
| `id` | yes | string |
| `version` | no | string |
| `spec_hash` | no | string |

The schema allows additional properties, so the rest of this contract is semantic guidance until schema expansion is verified.

## Accepted uses

| Use | Allowed? | Rule |
|---|---:|---|
| Showing trust posture on map, drawer, focus, story, or export surfaces | Yes | Must point to safe evidence/detail context. |
| Opening the Evidence Drawer or safe detail panel | Yes | Badge click should route to proof context where allowed. |
| Showing stale or unresolved state | Yes | Must not be styled as a pass. |
| Showing release/correction/freshness state | Yes | Must preserve caveat or blocked state when material. |
| Treating badge as evidence | No | EvidenceBundle and EvidenceRef own support. |
| Treating badge as policy decision | No | PolicyDecision/policy roots own decisions. |
| Treating badge as release approval | No | Release roots own publication state. |

## Exclusions

| Do not use this contract as | Correct home or behavior |
|---|---|
| Evidence or proof | Use EvidenceBundle, EvidenceRef, receipts, and proof roots. |
| Policy authority | Use PolicyDecision and policy roots. |
| Release authority | Use release contracts and release roots. |
| Visual-token authority | Use brand/style/design-token roots. |
| UI component implementation | Use UI/web/app roots. |
| Internal-store access path | Use governed API/released projections only. |

## Finite states

The architecture anchor defines a narrow trust-visible state family. This contract keeps that state family visible and non-authoritative.

| State | UI meaning | Required posture |
|---|---|---|
| `VERIFIED` | The surfaced category has passed its relevant checks. | May display as supported, but still route to evidence/detail. |
| `STALE` | The surfaced category has aged, drifted, or exceeded a tolerance. | Display caveat; do not treat as fresh. |
| `UNKNOWN` | Required checks could not be completed. | Display caveat; do not treat as pass. |
| `FAILED` | Required checks ran and failed. | Display failure/blocked state according to policy. |

Color alone must not be the only state indicator. Accessible labels and non-color indicators are required.

## Recommended UI fields

PROPOSED until schema expansion:

| Field | Meaning |
|---|---|
| `id` | Badge state identifier. |
| `version` | Badge state contract/object version. |
| `spec_hash` | Deterministic baseline hash. |
| `subject_ref` | Feature, layer, story node, drawer payload, answer, or export being badged. |
| `badge_family` | source_role, rights, sensitivity, review, freshness, release, correction, citation, or accepted family. |
| `state` | VERIFIED, STALE, UNKNOWN, FAILED. |
| `reason_code` | Public-safe reason for state. |
| `label` | Human-readable badge label. |
| `accessibility_label` | Assistive-technology label. |
| `detail_target_ref` | Evidence Drawer or safe detail target. |
| `evidence_refs` | Optional public-safe EvidenceRef pointers. |
| `policy_decision_refs` | Related policy decision refs. |
| `release_refs` | Related release state refs. |
| `caveats` | Public-safe caveats. |
| `updated_at` | Badge-state assembly/update time. |

## Validation expectations

NEEDS VERIFICATION:

- schema expansion beyond `id`, `version`, and `spec_hash`;
- final state vocabulary and badge-family vocabulary;
- validator path and CI wiring;
- fixtures for VERIFIED, STALE, UNKNOWN, FAILED;
- accessibility label and non-color indicator tests;
- Evidence Drawer click/detail behavior;
- policy/release/freshness/correction linkage;
- export/screenshot behavior.

## Open questions

- Should `TrustBadgeState` be the canonical object name or should it align with `TrustVisibleState` from architecture docs?
- Which badge families are mandatory for public map layers versus optional for internal surfaces?
- Which states are public-safe for sensitive domains?
- Should badge state be generated per response, cached, or emitted in published payloads?

## Rollback

Rollback is required if this contract becomes evidence authority, policy authority, release approval, proof storage, visual-design authority, UI implementation, internal-store access, or a way to hide unresolved or failed trust posture.

Rollback target for this expansion: previous scaffold blob SHA `5e92d12755ca7db74a77293e9880d0abb0c5c6a4`.

<p align="right"><a href="#top">Back to top</a></p>
