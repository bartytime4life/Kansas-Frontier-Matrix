<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-release-withdrawal-notice
title: contracts/release/withdrawal_notice.md — WithdrawalNotice Contract
type: contract
version: v0.3
status: draft; PROPOSED; schema-paired; thin-schema; fixture-validated; no-network; non-publisher
owners: OWNER_TBD — Release steward · Withdrawal steward · Correction steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Rights steward · Sensitivity steward · Review steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-08-23
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
  - ../../tests/validators/test_validate_withdrawal_notice.py
  - ../../.github/workflows/withdrawal-notice.yml
  - ../../docs/architecture/release-discipline.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../data/proofs/
  - ../../data/receipts/
notes:
  - "Paired schema verified at `schemas/contracts/v1/release/withdrawal_notice.schema.json`; schema status remains PROPOSED."
  - "The current schema is intentionally thin: only `id` is required and `additionalProperties` is true."
  - "A deterministic no-network validator, focused fixtures, focused tests, and a path-scoped workflow now prove only schema shape, bounded JSON safety, and fixture polarity."
  - "WithdrawalNotice records that a published/released object should no longer be served or relied on in the same way; it is not erasure and not silent deletion."
  - "Rollback target for v0.3 is the parent branch commit or previous blob SHA `3cb27571de43e49d3a9f9c1bee0b347f6f3e7753`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# WithdrawalNotice Contract

> `WithdrawalNotice` records that a previously published or release-candidate KFM object, release, layer, artifact, map surface, answer, or claim is withdrawn from public/restricted reliance. It exists to stop unsafe serving while preserving audit history. It is not deletion, erasure, a quiet edit, or proof that downstream invalidation has completed.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Object: WithdrawalNotice" src="https://img.shields.io/badge/object-WithdrawalNotice-0a7ea4">
  <img alt="Schema: thin" src="https://img.shields.io/badge/schema-thin__placeholder-orange">
  <img alt="Validation: bounded" src="https://img.shields.io/badge/validation-no--network__bounded-informational">
  <img alt="Mutation: no silent deletion" src="https://img.shields.io/badge/mutation-no__silent__deletion-critical">
  <img alt="Posture: fail closed" src="https://img.shields.io/badge/posture-fail__closed-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/release/withdrawal_notice.md`  
**Paired schema:** `schemas/contracts/v1/release/withdrawal_notice.schema.json`  
**Schema maturity:** thin / permissive / proposal-level  
**Bounded validator:** `tools/validators/release/validate_withdrawal_notice.py`  
**Focused test:** `tests/validators/test_validate_withdrawal_notice.py`  
**No-network workflow:** `.github/workflows/withdrawal-notice.yml`  
**Policy authority:** `policy/release/`, `policy/sensitivity/`, and rights/access policy roots, not this contract  
**Release artifact/process authority:** `release/`, not this contract  
**Truth posture:** CONFIRMED schema pairing, fixture lane, bounded validator, focused test, and no-network workflow · CONFIRMED release doctrine requires visible correction and rollback lineage · PROPOSED detailed withdrawal semantics until schema, policy, review, invalidation, emitter, and operational release integration are separately governed and proved

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Target semantic field families](#target-semantic-field-families) · [Field semantics](#field-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Implemented validation boundary](#implemented-validation-boundary) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

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

CONFIRMED by paired schema and bounded validator:

- `id` is required.
- `spec_hash` is optional and string-shaped if present.
- `version` is optional and string-shaped if present.
- Additional properties are currently allowed.
- duplicate JSON keys, non-object roots, malformed JSON, and non-finite JSON numbers fail closed;
- the focused fixture profile executes without network access or repository mutation.

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

## Implemented validation boundary

**CONFIRMED repository surface.** The current branch pairs this contract and schema with:

- `fixtures/release/withdrawal_notice/valid/minimal.json`;
- `fixtures/release/withdrawal_notice/invalid/missing_id.json`;
- `tools/validators/release/validate_withdrawal_notice.py`;
- `tests/validators/test_validate_withdrawal_notice.py`;
- `.github/workflows/withdrawal-notice.yml`.

The validator and focused test prove only:

- Draft 2020-12 schema validity;
- current required-field behavior;
- duplicate-key, malformed-input, non-object-root, and non-finite-number rejection;
- deterministic reason codes and exact fixture polarity;
- no-network, non-publisher execution.

The workflow does **not** prove or perform withdrawal, correction linkage, cache/index/tile/API/map/AI invalidation, restoration, rights or sensitivity policy, reviewer authority, release, deployment, promotion, or publication.

**NEEDS VERIFICATION / PROPOSED follow-up:**

- harden schema beyond the current `id`-only required surface;
- decide production-required fields and finite reason/type enums;
- add release/sensitivity/rights policy behavior;
- require CorrectionNotice linkage and public-safe notice handling where applicable;
- define accepted instance storage under the release root;
- emit proof/receipt records for withdrawal decisions and invalidation;
- add cache/index/tile/API/map/AI invalidation tests;
- define emergency withdrawal, post-facto review, lifting, and restoration rules;
- identify and validate live emitters and consumers.

---

## Fixtures

**CONFIRMED current bounded fixtures:**

| Fixture | Purpose |
|---|---|
| `valid/minimal.json` | Confirms the current schema permits the `id`-only minimum. |
| `invalid/missing_id.json` | Confirms the current required-field boundary fails closed. |

**PROPOSED semantic fixture expansion:**

| Fixture | Purpose |
|---|---|
| `valid/full_withdrawal_rights.json` | Mature withdrawal due to rights/source terms. |
| `valid/full_withdrawal_sensitivity.json` | Sensitive exact-location or living-person/DNA/geoprivacy withdrawal. |
| `valid/partial_redaction_withdrawal.json` | Partial withdrawal with generalized successor. |
| `valid/superseded_release_withdrawal.json` | Withdrawal because successor release supersedes artifact. |
| `valid/emergency_hold.json` | Emergency withdrawal pending review. |
| `governance-invalid/missing_affected_object.json` | Schema may pass; withdrawal governance should fail. |
| `governance-invalid/missing_correction_notice.json` | Public-facing withdrawal should fail without notice. |
| `governance-invalid/sensitive_reason_leak.json` | Ensures reason text does not leak sensitive details. |

All fixtures must remain synthetic or public-safe.

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

Rollback is required if this contract or validation lane is used to erase history, silently mutate or delete public state, bypass correction/release/policy/evidence/review gates, store artifacts, claim invalidation without receipts/proofs, leak sensitive withdrawal reasons, or authorize public API/UI/map/AI exposure directly.

Repository rollback for v0.3 is a revert of this dependency-closed PR, restoring contract blob `3cb27571de43e49d3a9f9c1bee0b347f6f3e7753`, removing `.github/workflows/withdrawal-notice.yml`, and restoring the prior navigational catalog projection. Reverting repository bytes does not itself restore or alter any release, deployment, promotion, publication, or external system state.

<p align="right"><a href="#top">Back to top</a></p>
