<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-release-rollback-card
title: contracts/release/rollback_card.md — RollbackCard Contract
type: contract
version: v0.2
status: draft; PROPOSED; schema-paired; thin-schema; rollback-target
owners: OWNER_TBD — Release steward · Rollback steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Correction steward · Review steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; release; rollback-card; rollback-target; correction-aware; release-gated; reversible; fail-closed; no-erasure
tags: [kfm, contracts, release, rollback-card, rollback, correction-notice, release-manifest, promotion-decision, reversibility, invalidation, restoration, fail-closed, no-silent-mutation]
related:
  - ./README.md
  - ./release_manifest.md
  - ./promotion_decision.md
  - ./withdrawal_notice.md
  - ./map_release_manifest.md
  - ./layer_manifest.md
  - ../correction/correction_notice.md
  - ../policy/policy_decision.md
  - ../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../policy/release/
  - ../../policy/promotion/
  - ../../release/
  - ../../fixtures/release/rollback_card/
  - ../../tools/validators/release/validate_rollback_card.py
  - ../../docs/architecture/release-discipline.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../data/proofs/
  - ../../data/receipts/
notes:
  - "Expanded from greenfield scaffold at `contracts/release/rollback_card.md`."
  - "Paired schema verified at `schemas/contracts/v1/release/rollback_card.schema.json`; schema status is PROPOSED."
  - "The current schema is a greenfield placeholder: only `id` is required and `additionalProperties` is true."
  - "This contract defines rollback-card semantic meaning only. It does not execute rollback, erase history, store release artifacts, write proofs/receipts, or authorize public surfaces."
  - "Rollback target for this expansion is previous blob SHA `c5a92ae1b809b662d93d55bf2cf7c72cd68c58f0`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# RollbackCard Contract

> `RollbackCard` records the explicit target, rationale, required checks, invalidation path, and restoration posture for rolling a published KFM surface back to a prior safe state. It exists to make rollback auditable and reversible; it is not deletion, erasure, silent mutation, or proof that rollback has already executed.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Object: RollbackCard" src="https://img.shields.io/badge/object-RollbackCard-0a7ea4">
  <img alt="Schema: thin" src="https://img.shields.io/badge/schema-thin__placeholder-orange">
  <img alt="Posture: reversible" src="https://img.shields.io/badge/posture-reversible-green">
  <img alt="Mutation: no silent edits" src="https://img.shields.io/badge/mutation-no__silent__edits-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/release/rollback_card.md`  
**Paired schema:** `schemas/contracts/v1/release/rollback_card.schema.json`  
**Schema maturity:** greenfield placeholder / thin / permissive  
**Validator path named by schema:** `tools/validators/release/validate_rollback_card.py` — NEEDS VERIFICATION for implementation/wiring  
**Policy authority:** `policy/release/`, not this contract  
**Release artifact/process authority:** `release/`, not this contract  
**Truth posture:** CONFIRMED schema pairing and thin field surface · CONFIRMED release doctrine treats rollback as post-PUBLISHED transition requiring RollbackCard, CorrectionNotice, ReleaseManifest reversion, and downstream invalidation · PROPOSED detailed fields until schema/fixtures/validator/policy/release integration are verified

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Target semantic field families](#target-semantic-field-families) · [Field semantics](#field-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`RollbackCard` is the semantic object that makes a rollback target explicit before or during a rollback event.

It answers:

- which published release, artifact, layer, claim, map surface, API response, catalog entry, or AI answer is affected;
- why rollback is needed;
- what prior release or state is the rollback target;
- which artifacts, caches, indexes, layers, derivatives, and public surfaces must be invalidated or restored;
- which evidence, policy, review, and correction records support the rollback;
- what users or downstream systems should bind to after rollback.

It does not answer:

- whether rollback has executed — that requires release process records, receipts, proofs, logs, and validation;
- whether the prior release is true — EvidenceBundle and release manifest support remain authoritative;
- whether public notice has been issued — CorrectionNotice or withdrawal/correction process owns that surface;
- whether erasure is allowed — rollback preserves audit history unless a separate legal/policy process governs removal.

---

## Meaning

A `RollbackCard` is a rollback plan and target binding. It is created when a published or release-candidate state must be restored, reverted, superseded, held, or made safe after a release defect, rights change, sensitivity discovery, evidence contradiction, validation failure, source withdrawal, policy defect, security issue, or operational failure.

Rollback is not silent mutation. The old release remains inspectable unless a separate governed removal/withholding policy applies. A rollback points clients and downstream systems to a safer prior state, records what must be invalidated, and links to the correction/notice pathway that explains why public state changed.

A rollback card may be created before release as a required target, or after publication as the object used to execute/review rollback.

---

## Schema-paired field surface

The paired schema is currently intentionally thin.

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `id` | yes | string | Canonical rollback card identifier. |
| `spec_hash` | no | string | Deterministic content/spec hash, if present. |
| `version` | no | string | Rollback card/object version, if present. |

Schema-confirmed posture:

- `id` is the only required field.
- `spec_hash` and `version` are optional.
- `additionalProperties` is currently `true`.

> [!WARNING]
> The detailed rollback semantics below are **PROPOSED** until the schema is hardened. Current schema permissiveness means an instance may validate while still being rollback-incomplete by governance standards.

---

## Target semantic field families

A mature `RollbackCard` should eventually model these field families explicitly or by resolvable refs.

| Field family | Meaning | Required posture |
|---|---|---|
| Identity | rollback card id, version, spec hash, card digest, canonicalization profile. | Deterministic and citable. |
| Trigger | defect, contradiction, rights change, sensitivity issue, validation failure, source withdrawal, security issue, policy failure. | Safe reason code; no sensitive payload leakage. |
| Affected release | current release/manifest/artifact/layer/claim/API/map/AI surface refs. | Must resolve. |
| Rollback target | prior release manifest, prior artifact set, prior layer version, prior catalog/triplet state, or null-withdrawn state. | Must resolve unless explicit emergency hold. |
| Evidence | EvidenceRefs/EvidenceBundle refs supporting rollback need. | Must resolve for non-emergency rollback. |
| Policy | PolicyDecision/PromotionDecision/release-policy refs. | Must record gate posture. |
| Correction link | CorrectionNotice/stale-state/withdrawal/supersession refs. | Required for public-surface change. |
| Invalidation | cache, CDN, tile, catalog, API, graph, vector index, search index, AI answer cache, downstream derivative invalidation list. | Must be explicit. |
| Restoration | target state, release manifest, artifacts, routes, indexes, and public notices after rollback. | Must be testable. |
| Review | reviewer, ticket, separation-of-duties state, emergency override if any. | Required for material rollback. |
| Attestations | signing/build/validation/provenance refs for target and rollback action. | Digest-bound where applicable. |
| Time | detected, decided, effective, executed, validated, public-noticed times. | Time kinds should be explicit. |

---

## Field semantics

### `id`

Canonical rollback card identifier.

Requirements:

- stable enough to cite from release manifests, correction notices, promotion decisions, incident records, receipts, proofs, and public notices where allowed;
- specific to a rollback target/action, not a mutable pointer to the newest rollback;
- safe to expose publicly when release/correction policy allows.

PROPOSED convention:

```text
rollback:<domain-or-surface>:<yyyy-mm-dd>:<sequence-or-hash>
```

### `spec_hash`

Deterministic hash claiming spec/content lineage for the rollback card.

Current schema makes it optional. Mature rollback cards should include a digest or spec hash so reviewers can verify the rollback target was not changed after approval.

### `version`

Rollback card version string.

Current schema makes it optional. Mature rollback cards should include a version or equivalent lineage marker to support supersession, correction, emergency updates, and audit.

---

## Invariants

CONFIRMED by paired schema:

- `id` is required.
- `spec_hash` is optional and string-shaped if present.
- `version` is optional and string-shaped if present.
- Additional properties are currently allowed.

PROPOSED semantic invariants:

- Rollback is a governed transition, not deletion or silent mutation.
- A rollback card must identify both the affected state and the rollback target, or explicitly mark emergency hold/withdrawal posture.
- A rollback card must link to a CorrectionNotice or equivalent public-safe notice for post-PUBLISHED public changes.
- The rollback target must be inspectable and verifiable before restoration.
- Downstream derivatives, caches, indexes, tiles, API responses, map surfaces, and AI answer caches must be invalidated or explicitly marked not affected.
- Evidence, policy, rights, sensitivity, review, and release context must resolve before non-emergency rollback completes.
- Rollback must preserve audit history; erasure requires a separate governed legal/policy process.
- A superseding rollback card must not silently mutate the prior card.

---

## Lifecycle role

`RollbackCard` applies at release planning and post-publication repair points:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Expected use:

| Lifecycle point | Role |
|---|---|
| CATALOG/TRIPLET → PUBLISHED | Required or referenced as rollback target before a material release. |
| PUBLISHED defect discovered | Identifies affected release state and rollback target. |
| PUBLISHED → prior release | Supplies rollback target/invalidation/restoration plan. |
| PUBLISHED → PUBLISHED′ correction | Links to CorrectionNotice and superseding ReleaseManifest where rollback is partial or correction-based. |
| PUBLISHED → withdrawn | Supports null/withheld target when no safe prior state exists. |

---

## Boundaries

| Boundary | Rule |
|---|---|
| Contract vs schema | This contract defines meaning; schema defines machine shape. |
| RollbackCard vs ReleaseManifest | RollbackCard identifies target/instructions; ReleaseManifest binds release contents. |
| RollbackCard vs CorrectionNotice | CorrectionNotice explains public correction/supersession/withdrawal; RollbackCard records rollback target/action context. |
| RollbackCard vs PromotionDecision | PromotionDecision may require rollback support; RollbackCard provides rollback target. |
| RollbackCard vs proof/receipt | RollbackCard references receipts/proofs; it is not proof of execution. |
| RollbackCard vs release artifacts | RollbackCard references artifacts; it does not store payloads. |
| RollbackCard vs public API/UI/map/AI | Public surfaces consume governed, released state after rollback; they do not execute rollback. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- harden schema beyond current `id`-only required surface;
- decide required fields for production rollback cards;
- validator existence and wiring for `tools/validators/release/validate_rollback_card.py`;
- fixture coverage under `fixtures/release/rollback_card/`;
- release policy behavior under `policy/release/`;
- CorrectionNotice linkage and public-safe notice requirements;
- release process storage under accepted release rollback homes;
- receipt/proof emission for rollback decisions and execution;
- cache/index/tile/API/map/AI invalidation tests;
- emergency rollback and post-facto review rules.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_minimal_schema.json` | Confirms current schema permits `id` only. |
| `valid_release_rollback.json` | Mature rollback with affected release, rollback target, evidence, policy, correction, invalidation, review. |
| `valid_map_tile_rollback.json` | Rollback of PMTiles/COG/map layer artifacts. |
| `valid_withdrawal_no_safe_prior.json` | Withdrawal/null target when no safe prior release exists. |
| `valid_emergency_hold.json` | Emergency hold pending review with explicit follow-up. |
| `invalid_missing_id.json` | Confirms current required field. |
| `governance_invalid_missing_target.json` | Schema may pass; rollback governance should fail. |
| `governance_invalid_missing_correction_notice.json` | Schema may pass; public-surface rollback should fail. |
| `governance_invalid_missing_invalidation.json` | Schema may pass; downstream leakage risk. |
| `governance_invalid_erasure_without_policy.json` | Ensures rollback is not silent erasure. |

Fixtures must use synthetic or safe refs only.

---

## Open questions

- Which fields should be required in the next rollback-card schema version?
- Should `RollbackCard` always require `CorrectionNotice`, or only after PUBLISHED exposure?
- Should emergency rollback allow temporary missing evidence/review with mandatory follow-up receipt?
- Which release root stores rollback-card instances?
- How should cache/CDN/tile/vector-index/AI-answer invalidation be represented?
- Should rollback cards be signed or DSSE-wrapped like release manifests?

---

## Rollback

Rollback is required if this contract is used to erase history, silently mutate published state, bypass release/correction/policy/evidence/review gates, store artifacts, claim rollback execution without receipts/proofs, or authorize public API/UI/map/AI exposure directly.

Rollback target for this expansion: previous blob SHA `c5a92ae1b809b662d93d55bf2cf7c72cd68c58f0`.

<p align="right"><a href="#top">Back to top</a></p>
