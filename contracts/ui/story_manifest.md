<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-story-manifest
title: contracts/ui/story_manifest.md — UI StoryManifest Contract
type: semantic-contract
version: v0.3
status: draft; PROPOSED; schema-stub-confirmed; ui-family; story-display-manifest; evidence-dependent; release-gated
owners: OWNER_TBD — UI steward · Story steward · Evidence steward · Runtime steward · Policy steward · Release steward · Schema steward · Accessibility steward · Docs steward
created: NEEDS VERIFICATION — greenfield scaffold existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; ui; story-manifest; projection; evidence-dependent; release-gated; no-sovereign-truth
tags: [kfm, contracts, ui, story-manifest, StoryManifest, story, narrative, EvidenceBundle, EvidenceRef, CitationValidationReport, PolicyDecision, ReleaseManifest, RuntimeResponseEnvelope]
related:
  - ./README.md
  - ./evidence_drawer_payload.md
  - ./citation_validation_report.md
  - ./focus_response.md
  - ../story/README.md
  - ../evidence/evidence_bundle.md
  - ../evidence/evidence_ref.md
  - ../evidence/citation_validation_report.md
  - ../runtime/runtime_response_envelope.md
  - ../policy/policy_decision.md
  - ../release/release_manifest.md
  - ../../schemas/contracts/v1/ui/story_manifest.schema.json
  - ../../policy/ui/
  - ../../policy/story/
  - ../../fixtures/ui/story_manifest/
notes:
  - "v0.3 strengthens navigation, repo fit, exclusions, state semantics, evidence ledger, and verification posture while preserving the accepted v0.2 boundary."
  - "A paired UI schema stub exists at `schemas/contracts/v1/ui/story_manifest.schema.json`; it requires only `id`, allows additional properties, and names this contract doc."
  - "The `contracts/story/README.md` lane defines story objects as evidence-dependent presentation objects and not sovereign truth."
  - "This file defines UI-facing meaning only. It is not story truth, release approval, EvidenceBundle closure, policy execution, proof storage, or UI implementation."
  - "Rollback target for this expansion is previous v0.2 blob SHA `34205a3f947c768208fc9378f2695628124bc183`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI StoryManifest Contract

> `StoryManifest` is the UI-facing manifest for a governed story surface. It tells the UI which story sections, map callouts, time windows, evidence references, caveats, and trust states may be rendered. It is a display contract, not a truth source.

<p>
  <img alt="Status: PROPOSED" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Family: UI" src="https://img.shields.io/badge/family-ui-0a7ea4">
  <img alt="Object: StoryManifest" src="https://img.shields.io/badge/object-StoryManifest-purple">
  <img alt="Schema: stub confirmed" src="https://img.shields.io/badge/schema-stub__confirmed-orange">
  <img alt="Boundary: display not truth" src="https://img.shields.io/badge/boundary-display__not__truth-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/ui/story_manifest.md`  
**Paired schema:** `schemas/contracts/v1/ui/story_manifest.schema.json`  
**Schema posture:** PROPOSED stub; required field `id` only; `additionalProperties: true`  
**Related story lane:** `contracts/story/README.md`  
**Truth posture:** CONFIRMED target existed as a UI scaffold and v0.2 contract draft · CONFIRMED paired UI schema stub exists and names this contract doc · CONFIRMED story lane treats stories as evidence-dependent presentation · NEEDS VERIFICATION for final schema, fixtures, validator, UI implementation, policy wiring, and release behavior

**Quick jumps:** [Purpose](#purpose) · [Repo fit](#repo-fit) · [Meaning](#meaning) · [Authority split](#authority-split) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended UI fields](#recommended-ui-fields) · [Story state relationship](#story-state-relationship) · [Evidence ledger](#evidence-ledger) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This contract defines how a UI story surface receives and renders a story manifest.

It answers:

- which story sections are in scope;
- which map and time context frame the story;
- which evidence, citation, policy, release, review, correction, and rollback references should remain visible when material;
- what caveats and trust states the UI must preserve.

It does not answer whether a claim is true, whether a release is approved, whether evidence is complete, or whether UI code is implemented.

## Repo fit

| Relationship | Path | Status |
|---|---|---|
| This semantic contract | `contracts/ui/story_manifest.md` | PROPOSED / current file |
| UI contract lane | `contracts/ui/README.md` | CONFIRMED adjacent lane guide |
| Story semantic lane | `contracts/story/README.md` | CONFIRMED related lane guide |
| Paired UI schema | `schemas/contracts/v1/ui/story_manifest.schema.json` | CONFIRMED permissive stub |
| UI policy home | `policy/ui/` | Referenced by schema; implementation depth NEEDS VERIFICATION |
| UI fixtures | `fixtures/ui/story_manifest/` | Referenced by schema; existence/coverage NEEDS VERIFICATION |

## Meaning

A `StoryManifest` is a governed projection for story playback.

```text
released story candidate
  -> evidence, citation, policy, review, and release checks
  -> StoryManifest
  -> UI story surface
```

The manifest organizes display. It does not create evidence, approve release, or make narrative text authoritative.

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| UI story manifest meaning | `contracts/ui/story_manifest.md` | This file. |
| Story object meaning | `contracts/story/` | Story/narrative semantic lane. |
| Evidence support | `contracts/evidence/` | EvidenceBundle and EvidenceRef support claims. |
| Citation checking | `contracts/evidence/citation_validation_report.md` and `contracts/ui/citation_validation_report.md` | Citation validation remains separate. |
| Runtime response | `contracts/runtime/runtime_response_envelope.md` | Runtime owns finite outcome envelopes. |
| Policy/admissibility | `policy/ui/`, `policy/story/`, `policy/evidence/` | Policy owns allow/restrict/abstain decisions. |
| Machine shape | `schemas/contracts/v1/ui/story_manifest.schema.json` | Current stub only. |
| UI rendering | UI/web/app roots | Rendering code stays outside contracts. |
| Release/correction/rollback | `release/` and release contracts | Publication state remains separate. |

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
| Driving a governed story surface | Yes | Must preserve evidence and release posture. |
| Ordering story sections | Yes | Order does not make claims true. |
| Binding story to map/time context | Yes | Must stay within governed context. |
| Showing caveats and no-data states | Yes | Trust state must remain visible. |
| Linking to evidence or citation reports | Conditional | Only display public-safe refs or summaries. |
| Treating manifest as release approval | No | Release roots own that. |
| Treating manifest as EvidenceBundle closure | No | EvidenceBundle owns that. |
| Treating manifest as story truth | No | Story remains evidence-dependent. |

## Exclusions

| Do not use this contract as | Correct home or behavior |
|---|---|
| Story truth authority | Use evidence, citation, policy, review, and release state. |
| Release approval | Use release contracts and release roots. |
| EvidenceBundle closure | Use EvidenceBundle. |
| Policy decision | Use policy roots and PolicyDecision contracts. |
| Proof or receipt storage | Use proof/receipt roots. |
| UI implementation | Use UI/web/app roots. |
| Internal-store access path | Use governed API/released projections only. |

## Recommended UI fields

PROPOSED until schema expansion:

| Field | Meaning |
|---|---|
| `id` | Story manifest identifier. |
| `version` | Manifest version. |
| `spec_hash` | Deterministic baseline hash. |
| `story_ref` | Story object or released story artifact reference. |
| `title` | Public-safe title. |
| `audience` | Intended audience. |
| `release_refs` | Release references. |
| `map_context_refs` | Map/time/layer context references. |
| `sections` | Ordered section references or projections. |
| `callouts` | Map callout references. |
| `timeline_events` | Time-aware event references. |
| `evidence_bundle_refs` | Supporting EvidenceBundle references. |
| `citation_validation_refs` | Citation validation references. |
| `policy_decision_refs` | Policy decision references. |
| `caveats` | Required limitations and uncertainty notes. |
| `review_refs` | Review references. |
| `correction_refs` | Correction or supersession references. |
| `rollback_ref` | Rollback reference if material. |
| `trust_badges` | Visible trust-state badges. |
| `accessibility_summary` | Assistive-technology summary. |

## Story state relationship

| State | UI meaning | Required posture |
|---|---|---|
| `ready` | Manifest points to released, cited, policy-safe sections. | Display with caveats/trust badges. |
| `partial` | Some sections cannot be shown or remain unresolved. | Display only safe sections and visible caveats. |
| `abstained` | Evidence/citation support is insufficient for the core claim. | Do not render as authoritative story truth. |
| `blocked` | Policy, release, sensitivity, or rights posture prevents display. | Show safe status without exposing withheld details. |
| `error` | Manifest/schema/runtime failure prevents safe playback. | Show diagnostic state only. |
| `superseded` | Story was corrected, withdrawn, or replaced. | Show correction/supersession posture and rollback/correction refs. |

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/ui/story_manifest.md` previous v0.2 | CONFIRMED | Existing baseline, field list, rollback target. | Did not fully satisfy the richer Markdown authoring pattern. |
| `schemas/contracts/v1/ui/story_manifest.schema.json` | CONFIRMED | Paired schema stub, required `id`, permissive additional properties. | Does not enforce full proposed field set. |
| `contracts/story/README.md` | CONFIRMED | Story objects are evidence-dependent presentation and not sovereign truth. | Does not finalize UI/story object split. |
| User-supplied Markdown Authoring Agent prompt | CONFIRMED source material | Presentation and evidence-first documentation requirements. | It is an authoring standard, not repo implementation proof. |

## Validation expectations

NEEDS VERIFICATION:

- schema expansion beyond `id`, `version`, and `spec_hash`;
- final UI/story home split;
- validator path and CI wiring;
- fixtures for ready, partial, abstained, blocked, error, corrected, and superseded cases;
- story player behavior;
- evidence/citation/policy/release linkage;
- accessibility behavior;
- correction and rollback behavior.

## Open questions

- Should `StoryManifest` live under `contracts/ui/`, `contracts/story/`, or a split model?
- Should manifests be released artifacts or generated projections?
- Which fields are public versus steward-only?
- Which story-state vocabulary is final?

## Rollback

Rollback is required if this contract becomes story truth authority, publication approval, EvidenceBundle closure, PolicyDecision, editorial approval, story player implementation, schema authority, proof storage, internal-store access, or a way to display non-release-safe story material.

Rollback target for this expansion: previous v0.2 blob SHA `34205a3f947c768208fc9378f2695628124bc183`.

<p align="right"><a href="#top">Back to top</a></p>
