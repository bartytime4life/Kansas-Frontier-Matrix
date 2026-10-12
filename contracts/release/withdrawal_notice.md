<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-release-withdrawal-notice
title: contracts/release/withdrawal_notice.md — WithdrawalNotice Contract
type: contract
version: v0.2
status: draft; PROPOSED; schema-paired; thin-schema; withdrawal-notice
owners: OWNER_TBD — Release steward · Withdrawal steward · Correction steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Rights steward · Sensitivity steward · Review steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; release; withdrawal-notice; post-publication; correction-aware; rights-aware; sensitivity-aware; fail-closed; no-erasure; no-silent-mutation
tags: [kfm, contracts, release, withdrawal-notice, withdrawal, correction-notice, release-manifest, rollback-card, public-notice, rights, sensitivity, stale, supersession, invalidation, no-silent-mutation]
related:
  - ./README.md
  - ./release_manifest.md
  - ./promotion_decision.md
  - ./rollback_card.md
  - ./map_release_manifest.md
  - ./layer_manifest.md
  - ./tile_artifact_manifest.md
  - ../correction/correction_notice.md
  - ../policy/policy_decision.md
  - ../../schemas/contracts/v1/release/withdrawal_notice.schema.json
  - ../../policy/release/
  - ../../policy/sensitivity/
  - ../../release/
  - ../../fixtures/release/withdrawal_notice/
  - ../../tools/validators/release/validate_withdrawal_notice.py
  - ../../docs/architecture/release-discipline.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../data/proofs/
  - ../../data/receipts/
notes:
  - "Expanded from greenfield scaffold at `contracts/release/withdrawal_notice.md`."
  - "Paired schema verified at `schemas/contracts/v1/release/withdrawal_notice.schema.json`; schema status is PROPOSED."
  - "The current schema is a greenfield placeholder: only `id` is required and `additionalProperties` is true."
  - "WithdrawalNotice records that a published/released object should no longer be served or relied on in the same way; it is not erasure and not silent deletion."
  - "Rollback target for this expansion is previous blob SHA `9e96a3171d58724ec09dfccd65630b5347163091`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# WithdrawalNotice Contract

> `WithdrawalNotice` records that a previously published or release-candidate KFM object, release, layer, artifact, map surface, answer, or claim is withdrawn from public/restricted reliance. It exists to stop unsafe serving while preserving audit history. It is not deletion, erasure, a quiet edit, or proof that downstream invalidation has completed.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Object: WithdrawalNotice" src="https://img.shields.io/badge/object-WithdrawalNotice-0a7ea4">
  <img alt="Schema: thin" src="https://img.shields.io/badge/schema-thin__placeholder-orange">
  <img alt="Mutation: no silent deletion" src="https://img.shields.io/badge/mutation-no__silent__deletion-critical">
  <img alt="Posture: fail closed" src="https://img.shields.io/badge/posture-fail__closed-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/release/withdrawal_notice.md`  
**Paired schema:** `schemas/contracts/v1/release/withdrawal_notice.schema.json`  
**Schema maturity:** greenfield placeholder / thin / permissive  
**Validator path named by schema:** `tools/validators/release/validate_withdrawal_notice.py` — NEEDS VERIFICATION for implementation/wiring  
**Policy authority:** `policy/release/`, `policy/sensitivity/`, rights/access policy roots, not this contract  
**Release artifact/process authority:** `release/`, not this contract  
**Truth posture:** CONFIRMED schema pairing and thin field surface · CONFIRMED CorrectionNotice covers withdrawn public posture and prevents silent mutation · CONFIRMED release doctrine requires correction/rollback artifacts after PUBLISHED · PROPOSED detailed fields until schema/fixtures/validator/policy/release integration are verified

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Target semantic field families](#target-semantic-field-families) · [Field semantics](#field-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`WithdrawalNotice` is the semantic object for a governed withdrawal from release/public reliance.

It answers:

- what release, artifact, layer, claim, map surface, API answer, catalog entry, or AI answer was withdrawn;
- why withdrawal occurred;
- whether the withdrawal is temporary, permanent, partial, restricted, redacted, superseded, or pending review;
- which evidence, rights, sensitivity, policy, review, correction, rollback, or source update supports the withdrawal;
- which downstream consumers, caches, indexes, maps, tiles, graphs, catalogs, and AI answer surfaces must stop relying on the withdrawn object;
- what replacement, successor, rollback target, or public-safe explanation applies.

It does not answer:

- whether the underlying content is destroyed;
- whether a legal erasure process has occurred;
- whether downstream invalidation has completed;
- whether the replacement content is true by itself;
- whether public clients may bypass release gates;
- whether AI output can summarize withdrawn content as authoritative.

---

## Meaning

A `WithdrawalNotice` is a release/correction trust object. It records that a previously released or candidate-released unit should no longer be served, cited, displayed, exported, or relied upon in the same way.

Withdrawal may be triggered by:

- rights or license uncertainty;
- source withdrawal or changed terms;
- sensitivity discovery;
- protected-location exposure;
- archaeology/cultural-sensitivity issue;
- living-person or DNA/genomics exposure;
- infrastructure/security risk;
- evidence contradiction;
- validation defect;
- policy defect;
- stale or superseded release;
- legal/governance hold;
- incorrect map/tile artifact;
- release integrity failure.

Withdrawal preserves auditability. It should explain safe public posture without leaking sensitive facts or private details.

---

## Schema-paired field surface

The paired schema is currently intentionally thin.

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `id` | yes | string | Canonical withdrawal notice identifier. |
| `spec_hash` | no | string | Deterministic content/spec hash, if present. |
| `version` | no | string | Withdrawal notice/object version, if present. |

Schema-confirmed posture:

- `id` is the only required field.
- `spec_hash` and `version` are optional.
- `additionalProperties` is currently `true`.

> [!WARNING]
> The detailed withdrawal semantics below are **PROPOSED** until the schema is hardened. Current schema permissiveness means an instance may validate while still being withdrawal-incomplete by governance standards.

---

## Target semantic field families

A mature `WithdrawalNotice` should eventually model these field families explicitly or by resolvable refs.

| Field family | Meaning | Required posture |
|---|---|---|
| Identity | withdrawal notice id, version, spec hash, notice digest, canonicalization profile. | Deterministic and citable. |
| Affected object | release, artifact, layer, claim, map surface, API response, catalog record, AI answer, source descriptor, or bundle refs. | Must resolve. |
| Withdrawal reason | rights, sensitivity, evidence, validation, source withdrawal, policy defect, legal hold, stale/superseded state, security risk. | Safe reason code; no sensitive payload leakage. |
| Withdrawal type | temporary, permanent, partial, full, restricted, redacted, superseded, embargoed, emergency hold. | Finite enum recommended. |
| Effective posture | not served, generalized, restricted, withheld, superseded, stale, pending review, rollback target. | Must be explicit. |
| Evidence | EvidenceRefs/EvidenceBundle/source-update refs supporting withdrawal. | Must resolve except emergency hold with follow-up. |
| Policy | PolicyDecision/release/sensitivity/rights policy refs. | Must record gate posture. |
| Correction link | CorrectionNotice/stale-state/supersession refs. | Required for public-facing withdrawal. |
| Rollback/successor | prior release, successor release, null target, rollback card, or public-safe replacement refs. | Required when applicable. |
| Invalidation | cache, CDN, tile, catalog, API, graph, vector index, search index, AI answer cache, downstream derivative invalidation list. | Must be explicit. |
| Review | reviewer, steward, ticket, separation-of-duties state, emergency override if any. | Required for material withdrawal. |
| Time | detected, decided, effective, public-noticed, invalidated, reviewed, lifted times. | Time kinds should be explicit. |

---

## Field semantics

### `id`

Canonical withdrawal notice identifier.

Requirements:

- stable enough to cite from release manifests, correction notices, rollback cards, public notices, receipts, proofs, and affected-object metadata where allowed;
- specific to a withdrawal event, not a mutable pointer;
- safe to expose publicly when release/correction/sensitivity policy allows.

PROPOSED convention:

```text
withdrawal:<domain-or-surface>:<yyyy-mm-dd>:<sequence-or-hash>
```

### `spec_hash`

Deterministic hash claiming spec/content lineage for the withdrawal notice.

Current schema makes it optional. Mature withdrawal notices should include a digest or spec hash so reviewers can verify the withdrawal notice was not changed after review.

### `version`

Withdrawal notice version string.

Current schema makes it optional. Mature withdrawal notices should include a version or equivalent lineage marker to support supersession, correction, emergency updates, review, and audit.

---

## Invariants

CONFIRMED by paired schema:

- `id` is required.
- `spec_hash` is optional and string-shaped if present.
- `version` is optional and string-shaped if present.
- Additional properties are currently allowed.

PROPOSED semantic invariants:

- Withdrawal is not deletion, erasure, or silent mutation.
- A withdrawal notice must identify the affected released/candidate object or explicitly mark discovery as incomplete under emergency hold.
- Public-facing withdrawal must link to a CorrectionNotice or equivalent public-safe notice.
- Withdrawal reason must be safe to expose and must not leak sensitive coordinates, living-person data, DNA/genomics, security details, or restricted source content.
- Downstream derivatives, caches, indexes, tiles, APIs, maps, and AI answer caches must be invalidated or explicitly marked unaffected.
- Rights, sensitivity, evidence, policy, review, and release context must resolve before non-emergency withdrawal is considered closed.
- Lifting a withdrawal requires a new reviewed notice or superseding release state, not silent reactivation.
- Withdrawal preserves audit history unless a separate governed removal process applies.

---

## Lifecycle role

`WithdrawalNotice` applies when a released or candidate-released object must stop being relied upon:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Expected use:

| Lifecycle point | Role |
|---|---|
| CATALOG/TRIPLET candidate | May hold or withdraw a candidate from release eligibility before publication. |
| PUBLISHED defect discovered | Records object must no longer be served/cited/displayed as before. |
| PUBLISHED → withdrawn | Withdraws public/restricted surface and points to successor, rollback, null target, or review path. |
| PUBLISHED → PUBLISHED′ correction | Links withdrawal to correction/supersession when replacement exists. |
| Withdrawn → restored | Requires reviewed lifting notice, successor release, or rollback validation. |

---

## Boundaries

| Boundary | Rule |
|---|---|
| WithdrawalNotice vs CorrectionNotice | WithdrawalNotice records withdrawal posture; CorrectionNotice explains the public correction/trust modification pathway. |
| WithdrawalNotice vs RollbackCard | WithdrawalNotice can point to rollback; RollbackCard defines rollback target/action context. |
| WithdrawalNotice vs ReleaseManifest | ReleaseManifest binds release contents; WithdrawalNotice changes reliance posture or successor/withdrawal lineage. |
| WithdrawalNotice vs policy | Policy decides admissibility and exposure; notice records withdrawal semantics. |
| WithdrawalNotice vs erasure | Withdrawal is not deletion; erasure/removal requires separate legal/policy process. |
| WithdrawalNotice vs public surface | Public API/UI/map/AI must consume governed withdrawal state; they do not execute withdrawal. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- harden schema beyond current `id`-only required surface;
- decide required fields for production withdrawal notices;
- validator existence and wiring for `tools/validators/release/validate_withdrawal_notice.py`;
- fixture coverage under `fixtures/release/withdrawal_notice/`;
- release/sensitivity/rights policy behavior;
- CorrectionNotice linkage and public-safe notice requirements;
- release process storage under accepted release withdrawal homes;
- receipt/proof emission for withdrawal decisions and invalidation;
- cache/index/tile/API/map/AI invalidation tests;
- emergency withdrawal and post-facto review rules;
- lifting/restoration rules.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_minimal_schema.json` | Confirms current schema permits `id` only. |
| `valid_full_withdrawal_rights.json` | Mature withdrawal due to rights/source terms. |
| `valid_full_withdrawal_sensitivity.json` | Sensitive exact-location or living-person/DNA/geoprivacy withdrawal. |
| `valid_partial_redaction_withdrawal.json` | Partial withdrawal with generalized successor. |
| `valid_superseded_release_withdrawal.json` | Withdrawal because successor release supersedes artifact. |
| `valid_emergency_hold.json` | Emergency withdrawal pending review. |
| `invalid_missing_id.json` | Confirms current required field. |
| `governance_invalid_missing_affected_object.json` | Schema may pass; withdrawal governance should fail. |
| `governance_invalid_missing_correction_notice.json` | Public-facing withdrawal should fail without notice. |
| `governance_invalid_sensitive_reason_leak.json` | Ensures reason text does not leak sensitive details. |

Fixtures must use synthetic or safe refs only.

---

## Open questions

- Which fields should be required in the next withdrawal-notice schema version?
- Should `WithdrawalNotice` live only under release, or should correction own it as a subtype?
- Should all public-facing withdrawals require a `CorrectionNotice`, or only post-PUBLISHED withdrawals?
- What is the governed process for lifting a withdrawal?
- How should emergency withdrawal balance immediate public safety with post-facto evidence/review closure?
- Which release root stores withdrawal notice instances?

---

## Rollback

Rollback is required if this contract is used to erase history, silently mutate or delete public state, bypass correction/release/policy/evidence/review gates, store artifacts, claim invalidation without receipts/proofs, leak sensitive withdrawal reasons, or authorize public API/UI/map/AI exposure directly.

Rollback target for this expansion: previous blob SHA `9e96a3171d58724ec09dfccd65630b5347163091`.

<p align="right"><a href="#top">Back to top</a></p>
