<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-story-node
title: contracts/ui/story_node.md — UI StoryNode Contract
type: semantic-contract
version: v0.2
status: draft; PROPOSED; schema-stub-confirmed; ui-family; story-node; evidence-dependent; release-gated
owners: OWNER_TBD — UI steward · Story steward · Evidence steward · Runtime steward · Policy steward · Release steward · Schema steward · Accessibility steward · Docs steward
created: NEEDS VERIFICATION — greenfield scaffold existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; ui; story-node; projection; evidence-dependent; no-sovereign-truth
tags: [kfm, contracts, ui, story-node, StoryNode, story-manifest, story, narrative, EvidenceBundle, EvidenceRef, CitationValidationReport, PolicyDecision, ReleaseManifest]
related:
  - ./README.md
  - ./story_manifest.md
  - ./evidence_drawer_payload.md
  - ./citation_validation_report.md
  - ../story/README.md
  - ../evidence/evidence_bundle.md
  - ../evidence/evidence_ref.md
  - ../evidence/citation_validation_report.md
  - ../runtime/runtime_response_envelope.md
  - ../policy/policy_decision.md
  - ../release/release_manifest.md
  - ../../schemas/contracts/v1/ui/story_node.schema.json
  - ../../policy/ui/
  - ../../policy/story/
  - ../../fixtures/ui/story_node/
notes:
  - "Expanded from a PROPOSED greenfield scaffold at `contracts/ui/story_node.md`."
  - "A paired UI schema stub exists at `schemas/contracts/v1/ui/story_node.schema.json`; it requires only `id`, allows additional properties, and names this contract doc."
  - "`contracts/ui/story_manifest.md` defines StoryManifest as a governed display manifest, not a truth source."
  - "`contracts/story/README.md` defines story objects as evidence-dependent presentation objects and not sovereign truth."
  - "Rollback target for this expansion is previous scaffold blob SHA `84e128097ec0fdbce9a6186ee1b77bc66118a246`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI StoryNode Contract

> `StoryNode` is a UI-facing unit inside a governed story surface. It represents one renderable story section, callout, timeline item, evidence note, caveat, or transition in a `StoryManifest`. It is a display node, not story truth, not EvidenceBundle closure, not release approval, not policy execution, and not UI implementation.

<p>
  <img alt="Status: PROPOSED" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Family: UI" src="https://img.shields.io/badge/family-ui-0a7ea4">
  <img alt="Object: StoryNode" src="https://img.shields.io/badge/object-StoryNode-purple">
  <img alt="Schema: stub confirmed" src="https://img.shields.io/badge/schema-stub__confirmed-orange">
  <img alt="Boundary: display node not truth" src="https://img.shields.io/badge/boundary-display__node__not__truth-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/ui/story_node.md`  
**Paired schema:** `schemas/contracts/v1/ui/story_node.schema.json`  
**Schema posture:** PROPOSED stub; required field `id` only; `additionalProperties: true`  
**Parent UI manifest:** `contracts/ui/story_manifest.md`  
**Related story lane:** `contracts/story/README.md`  
**Truth posture:** CONFIRMED target was a greenfield scaffold · CONFIRMED paired UI schema stub exists and names this contract doc · CONFIRMED StoryManifest is a governed UI display manifest · CONFIRMED story lane treats stories as evidence-dependent presentation · NEEDS VERIFICATION for final schema, fixtures, validator, UI implementation, policy wiring, and release behavior

**Quick jumps:** [Purpose](#purpose) · [Repo fit](#repo-fit) · [Meaning](#meaning) · [Authority split](#authority-split) · [Schema posture](#schema-posture) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Recommended UI fields](#recommended-ui-fields) · [Node state relationship](#node-state-relationship) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

This contract defines how an individual UI story node is interpreted inside a governed story surface.

It answers:

- what kind of story unit the UI may render;
- which evidence, citation, policy, review, release, correction, and rollback references the node carries;
- how node-level caveats and trust state must remain visible;
- how a node relates to the parent `StoryManifest`.

It does not answer whether a claim is true, whether release is approved, whether evidence is complete, or whether UI code is implemented.

## Repo fit

| Relationship | Path | Status |
|---|---|---|
| This semantic contract | `contracts/ui/story_node.md` | PROPOSED / current file |
| Parent manifest contract | `contracts/ui/story_manifest.md` | CONFIRMED related UI display manifest |
| Story semantic lane | `contracts/story/README.md` | CONFIRMED related lane guide |
| Paired UI schema | `schemas/contracts/v1/ui/story_node.schema.json` | CONFIRMED permissive stub |
| UI policy home | `policy/ui/` | Referenced by schema; implementation depth NEEDS VERIFICATION |
| UI fixtures | `fixtures/ui/story_node/` | Referenced by schema; existence/coverage NEEDS VERIFICATION |

## Meaning

A `StoryNode` is one renderable unit in a governed story display.

```text
StoryManifest
  -> ordered StoryNode entries
  -> each node carries display type + refs + trust posture
  -> UI renders only policy-safe node content
```

The node organizes display. It does not create evidence, approve release, or make narrative text authoritative.

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| UI story node meaning | `contracts/ui/story_node.md` | This file. |
| Story manifest meaning | `contracts/ui/story_manifest.md` | Parent manifest that orders/selects nodes. |
| Story object meaning | `contracts/story/` | Story/narrative semantic lane. |
| Evidence support | `contracts/evidence/` | EvidenceBundle and EvidenceRef support claims. |
| Citation checking | `contracts/evidence/citation_validation_report.md` and `contracts/ui/citation_validation_report.md` | Citation validation remains separate. |
| Runtime response | `contracts/runtime/runtime_response_envelope.md` | Runtime owns finite outcome envelopes. |
| Policy/admissibility | `policy/ui/`, `policy/story/`, `policy/evidence/` | Policy owns allow/restrict/abstain decisions. |
| Machine shape | `schemas/contracts/v1/ui/story_node.schema.json` | Current stub only. |
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
| Rendering one story section or callout | Yes | Must preserve evidence and release posture. |
| Ordering nodes in a manifest | Yes | Order does not make claims true. |
| Binding a node to map/time context | Yes | Must stay within governed context. |
| Showing node-level caveats or no-data states | Yes | Trust state must remain visible. |
| Linking to EvidenceDrawerPayload or citation reports | Conditional | Only display public-safe refs or summaries. |
| Treating a node as release approval | No | Release roots own that. |
| Treating a node as EvidenceBundle closure | No | EvidenceBundle owns that. |
| Treating a node as story truth | No | Story remains evidence-dependent. |

## Exclusions

| Do not use this contract as | Correct home or behavior |
|---|---|
| Story truth authority | Use evidence, citation, policy, review, and release state. |
| StoryManifest replacement | Use `contracts/ui/story_manifest.md`. |
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
| `id` | Story node identifier. |
| `version` | Node contract/object version. |
| `spec_hash` | Deterministic baseline hash. |
| `manifest_ref` | Parent StoryManifest reference. |
| `node_type` | section, callout, timeline_event, caveat, evidence_note, transition, or accepted type. |
| `order_index` | Stable ordering within the manifest. |
| `title` | Public-safe node title. |
| `body_ref` | Reference to released or governed node text/projection. |
| `map_context_refs` | Map/time/layer context references. |
| `evidence_bundle_refs` | Supporting EvidenceBundle references. |
| `citation_validation_refs` | Citation validation references. |
| `policy_decision_refs` | Policy decision references. |
| `caveats` | Required limitations and uncertainty notes. |
| `correction_refs` | Correction or supersession references. |
| `rollback_ref` | Rollback reference if material. |
| `trust_badges` | Visible trust-state badges. |
| `accessibility_label` | Assistive-technology label for the node. |

## Node state relationship

| State | UI meaning | Required posture |
|---|---|---|
| `ready` | Node points to released, cited, policy-safe content. | Display with caveats/trust badges. |
| `partial` | Some node content cannot be shown or remains unresolved. | Display only safe content and visible caveats. |
| `abstained` | Evidence/citation support is insufficient for the node claim. | Do not render as authoritative story truth. |
| `blocked` | Policy, release, sensitivity, or rights posture prevents display. | Show safe status without exposing withheld details. |
| `error` | Node/schema/runtime failure prevents safe display. | Show diagnostic state only. |
| `superseded` | Node was corrected, withdrawn, or replaced. | Show correction/supersession posture and rollback/correction refs. |

## Validation expectations

NEEDS VERIFICATION:

- schema expansion beyond `id`, `version`, and `spec_hash`;
- final UI/story home split;
- validator path and CI wiring;
- fixtures for ready, partial, abstained, blocked, error, corrected, and superseded node cases;
- story player behavior;
- evidence/citation/policy/release linkage;
- accessibility behavior;
- correction and rollback behavior.

## Open questions

- Should `StoryNode` live under `contracts/ui/`, `contracts/story/`, or a split model?
- Should node text be embedded, referenced, or always generated from a released story artifact?
- Which node types are canonical?
- Which node fields are public versus steward-only?
- Which node-state vocabulary is final?

## Rollback

Rollback is required if this contract becomes story truth authority, StoryManifest replacement, publication approval, EvidenceBundle closure, PolicyDecision, editorial approval, story player implementation, schema authority, proof storage, internal-store access, or a way to display non-release-safe story material.

Rollback target for this expansion: previous scaffold blob SHA `84e128097ec0fdbce9a6186ee1b77bc66118a246`.

<p align="right"><a href="#top">Back to top</a></p>
