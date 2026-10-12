<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/agriculture/rollback-runbook
title: Agriculture — Rollback, Withdrawal, and Recovery Runbook
type: runbook; operational-procedure; domain-lane; non-authoritative
version: v0.2
status: draft; repository-grounded; rollback-card-validator-present; agriculture-drill-held; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Agriculture, release, rollback, correction, evidence, rights/sensitivity, and independent-review stewards"
created: 2026-05-13
updated: 2026-08-23
policy_label: public-review; agriculture; rollback; withdrawal; correction; fail-closed; no-publication-authority
current_path: docs/runbooks/agriculture/ROLLBACK_RUNBOOK.md
owning_root: docs/
responsibility: >
  Provide the repository-grounded human procedure for proposing, reviewing,
  executing, verifying, and correcting an Agriculture rollback or withdrawal
  without granting release, policy, evidence, review, deployment, or publication authority.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: same-path update; no new or parallel authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 265b99b81f9526a885caaf799e17c89b5424f9f2
  prior_blob: 720e0c768343af90ed35533e488dceaec86bdbf2
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  inspected_surfaces:
    - docs/runbooks/README.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - contracts/release/rollback_card.md
    - schemas/contracts/v1/release/rollback_card.schema.json
    - tools/validators/release/validate_rollback_card.py
    - tests/validators/test_validate_rollback_card.py
    - tests/domains/agriculture/rollback_drill/README.md
    - release/agriculture/README.md
related:
  - ../README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/agriculture/DATA_LIFECYCLE.md
  - ../../domains/agriculture/SENSITIVITY.md
  - ../../../contracts/release/rollback_card.md
  - ../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../tools/validators/release/validate_rollback_card.py
  - ../../../tests/validators/test_validate_rollback_card.py
  - ../../../tests/domains/agriculture/rollback_drill/README.md
  - ../../../release/agriculture/README.md
  - ../../../release/rollback_cards/README.md
  - ../../../release/correction_notices/README.md
  - ../../../release/manifests/README.md
tags: [kfm, agriculture, runbook, rollback, withdrawal, correction, release, governance, fail-closed]
notes:
  - "v0.2 replaces speculative release paths, stale rollback-card field claims, and implied execution maturity with current repository evidence."
  - "The shared release-family RollbackCard contract, schema, validator, fixtures, and focused tests are present; candidate validation remains non-executing and non-authoritative."
  - "The Agriculture rollback-drill lane remains README-only and documents missing executable drill proof, workflow TODOs, and remaining schema/home conflict; production rollback readiness is therefore not established."
  - "This document changes no release record, alias, fixture, contract, schema, policy, validator, workflow, receipt, proof, lifecycle object, deployment, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Agriculture — Rollback, Withdrawal, and Recovery Runbook

> **Recover an Agriculture public surface by using verified release identity, evidence, policy, review, correction, invalidation, and rollback targets—never by silently rewriting released bytes or treating a prior version as safe by default.**

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-state)
[![RollbackCard validator: present](https://img.shields.io/badge/RollbackCard%20validator-present-1f883d?style=flat-square)](#current-repository-state)
[![Agriculture rollback drill: HOLD](https://img.shields.io/badge/Agriculture%20drill-HOLD-d4a72c?style=flat-square)](#current-repository-state)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-non-effects)

> [!IMPORTANT]
> **Rollback documentation is not rollback authority.** The shared release-family `RollbackCard` profile is implemented as a closed, fixture-first candidate schema with a no-network validator and focused tests. That proves candidate shape and local consistency only; it does not approve or execute rollback, mutate a public alias, issue a correction, invalidate caches, release anything, or publish anything.

> [!CAUTION]
> **Agriculture rollback readiness remains held.** `tests/domains/agriculture/rollback_drill/` is currently README-only in repository evidence and records missing executable drill proof, TODO-only workflow behavior, unresolved release-plane/data-plane questions, and historical conflict around parallel rollback schema surfaces. Do not represent the Agriculture lane as operationally rehearsed or production-ready.

> [!WARNING]
> A rollback target can be older and still be unsafe. Rights may have changed, source roles may have been corrected, sensitivity rules may have tightened, evidence may no longer resolve, or downstream consumers may have changed. Revalidate the target under current governing rules before any recovery action.

**Quick navigation:** [Purpose](#1-purpose) · [Scope](#2-scope--non-goals) · [Placement](#3-repo-fit--placement) · [State](#current-repository-state) · [Triggers](#5-trigger-and-containment) · [Preconditions](#6-pre-rollback-preconditions) · [Decision](#7-candidate-decision-and-review) · [Execution](#8-execution-sequence) · [Invalidation](#9-downstream-invalidation) · [Agriculture rules](#10-agriculture-specific-constraints) · [Verification](#11-post-rollback-verification) · [Outcomes](#12-finite-outcomes-and-reason-codes) · [Drills](#13-drills-and-rehearsal) · [Rollback of this runbook](#14-runbook-change-rollback) · [Anti-patterns](#15-anti-patterns) · [Related](#16-related-surfaces) · [Evidence](#17-evidence-basis)

---

## 1. Purpose

This runbook defines the **human recovery procedure** for an Agriculture release whose current public or release-facing state is defective, unsafe, stale, unsupported, or otherwise no longer admissible.

It answers five bounded questions:

1. When should Agriculture use rollback, withdrawal, hold, or a forward correction?
2. Which current repository objects and checks must be resolved before action?
3. Which actions belong to release, correction, evidence, policy, review, or data invalidation authorities rather than this runbook?
4. How should Agriculture-specific rights, sensitivity, source-role, time, and spatial-support risks affect recovery?
5. What evidence is required before calling a recovery complete?

The governing recovery pattern is:

```text
problem detected
  -> contain unsafe exposure if authorized
  -> resolve affected release + current support
  -> validate RollbackCard candidate
  -> obtain required policy/review/release decisions
  -> withdraw, hold, or restore through governed release machinery
  -> invalidate/rebuild dependent derivatives
  -> emit correction/supersession records when required
  -> verify public-safe state + audit continuity
  -/> silent mutation, hidden deletion, or direct publication
```

A runbook explains the procedure. It does not create the underlying authority records or execute release state by documentation alone.

[Back to top](#top)

---

## 2. Scope & non-goals

### In scope

- Recovery planning for a released or release-candidate Agriculture surface.
- `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, and `ERROR` candidate handling using the shared release-family `RollbackCard` profile.
- Agriculture-specific containment, rights/sensitivity checks, source-role checks, temporal checks, spatial-support checks, and evidence checks.
- Downstream invalidation and re-derivation planning for released derivatives such as tiles, catalogs, triplets, search/vector indexes, API caches, CDN state, AI caches, and other dependent products.
- Correction/supersession obligations for previously exposed claims.
- Verification and audit-preservation requirements after recovery.

### Non-goals

- Approving a rollback or acting as release authority.
- Treating a schema-valid `RollbackCard` as an approved or executed rollback.
- Choosing a new canonical schema, contract, policy, or data home.
- Activating a source or connector.
- Writing directly to `PUBLISHED` or equivalent public state.
- Deleting a failing release, receipt, proof, correction record, or audit trail to make recovery appear clean.
- Replacing required human or policy-significant review.
- Claiming that Agriculture rollback drills, public alias switching, invalidators, release signing, deployment, or production recovery are implemented when current evidence does not prove them.

[Back to top](#top)

---

<a id="authority-and-non-effects"></a>

## 3. Repo fit & placement

**Placement outcome: `PLACE` — CONFIRMED for this same-path update.**

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). The parent [`docs/runbooks/` index](../README.md) identifies `docs/runbooks/` as the operational-procedure lane under the `docs/` responsibility root and confirms Agriculture as one of the tracked domain segments.

| Property | Current result |
|---|---|
| Path | `docs/runbooks/agriculture/ROLLBACK_RUNBOOK.md` |
| Authority owner | `docs/` — human-facing operational procedure |
| Scope | Agriculture domain lane |
| Path state | Existing tracked path; same-path modernization |
| Structural effect | None; no create, move, rename, split, mirror, or delete |
| Review route | `@bartytime4life` through repository review routing |
| Independent stewardship | `NEEDS VERIFICATION` |
| Release/publication effect | None |

This file may cite contracts, schemas, validators, fixtures, release records, evidence, policy, review, correction, and recovery tools. It cannot replace any of them.

[Back to top](#top)

---

<a id="current-repository-state"></a>

## 4. Current repository state

The following observations are pinned to `main@265b99b81f9526a885caaf799e17c89b5424f9f2`.

| Surface | CONFIRMED current evidence | Bounded conclusion |
|---|---|---|
| Shared RollbackCard contract | `contracts/release/rollback_card.md` defines semantic meaning and non-authority boundaries | Shared release-family semantics exist |
| Shared RollbackCard schema | `schemas/contracts/v1/release/rollback_card.schema.json` is closed, version `1.0.0`, and fixture-first | Machine shape is defined for candidate cards |
| Shared RollbackCard validator | `tools/validators/release/validate_rollback_card.py` performs no-network shape and local-consistency checks | Candidate validation is executable and bounded |
| Focused validator tests | `tests/validators/test_validate_rollback_card.py` checks schema validity, positive/negative fixtures, CLI profile, duplicate keys, non-finite numbers, and missing files | The validator has focused executable coverage |
| Candidate dispositions | `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, `ERROR` | Recovery candidates have a finite shared vocabulary |
| Governance flags | Candidate profile requires authority/review/policy/execution/public-mutation flags to remain false | Candidate validation cannot claim operational authority |
| Agriculture rollback drill | `tests/domains/agriculture/rollback_drill/README.md` remains documentation-only at its inspected checkpoint | Agriculture-specific executable drill proof is not established |
| Agriculture drill concerns | That README records TODO-only workflow behavior, missing executable drill implementation, and unresolved recovery topology questions | Operational readiness remains `HOLD` / `NEEDS VERIFICATION` |
| Release/public state mutation | Not proved by the runbook or candidate validator | Production rollback execution remains `UNKNOWN` unless proven from owning runtime/release evidence |

### What changed since the prior runbook text

The prior runbook described the RollbackCard field surface and multiple release homes as `PROPOSED`, even though current repository evidence now contains a shared contract, closed schema, validator, fixtures, and focused tests. It also implied more execution maturity than the Agriculture drill lane currently proves.

This revision therefore:

- points to the current shared release-family contract and schema instead of restating a competing shape;
- uses the validator's actual candidate dispositions, reason codes, invalidation classes, and authority limits;
- separates **candidate validation** from **rollback decision** and **rollback execution**;
- keeps Agriculture drill readiness on `HOLD` until executable proof exists;
- removes unverified kill-switch, feature-flag, alias-mutation, workflow, and publication claims as mandatory current behavior;
- preserves withdrawal, correction, downstream invalidation, evidence closure, rights/sensitivity, source-role, audit, and rollback invariants.

[Back to top](#top)

---

## 5. Trigger and containment

Start this procedure when a released or release-facing Agriculture product is suspected of violating evidence, policy, rights, sensitivity, temporal, spatial-support, source-role, integrity, compatibility, or release constraints.

Common triggers include:

| Trigger | Example Agriculture risk | Initial posture |
|---|---|---|
| `RELEASE_DEFECT` | Wrong release contents, incorrect current pointer, broken manifest linkage | `HOLD` pending release verification |
| `EVIDENCE_CONTRADICTION` | Public claim no longer resolves to admissible evidence | `ABSTAIN` or withdrawal pressure |
| `RIGHTS_CHANGE` | Source terms change or redistribution permission is narrowed | Fail closed; policy/review required |
| `SENSITIVITY_DISCOVERY` | Field, operator, parcel, well, or private-party detail was exposed | Contain exposure; do not substitute style hiding for data protection |
| `VALIDATION_FAILURE` | A released derivative no longer satisfies current validation | `HOLD` or withdrawal until corrected |
| `SOURCE_WITHDRAWAL` | A supporting source is no longer available or admissible | Reassess evidence closure and derived outputs |
| `POLICY_FAILURE` | Current policy denies a previously admissible public surface | `DENY` or withdrawal pressure |
| `SECURITY_ISSUE` | Public delivery can leak protected state or internal references | Contain through the authorized operational control plane |
| `OPERATIONAL_FAILURE` | Cache, index, tile, alias, or delivery state is inconsistent | `HOLD` until impact is bounded |
| `EMERGENCY_HOLD` | A steward requires immediate bounded containment | Hold without inventing a replacement target |
| `INSUFFICIENT_EVIDENCE` | Prior target cannot prove current evidence support | `ABSTAIN` / `HOLD` |
| `INPUT_INVALID` | Candidate request itself is malformed or ambiguous | `ERROR`; no state change |

These reason codes are the current shared `RollbackCard` trigger vocabulary. Additional narrative may explain the Agriculture context, but do not invent a second competing machine vocabulary in this runbook.

### Containment rule

If public exposure is actively unsafe, use only an already-authorized operational containment mechanism owned by the relevant release/runtime system. This runbook does not assume that a kill switch, alias swap, feature flag, CDN purge, route disable, or cache control exists unless current owning-surface evidence proves it.

Containment is not rollback completion. Preserve the affected release identity and audit trail while the governed recovery decision is assembled.

[Back to top](#top)

---

## 6. Pre-rollback preconditions

Before a rollback or withdrawal candidate advances beyond documentation and local validation, confirm the following.

### Release identity and target

- [ ] The affected release reference resolves through the current release authority.
- [ ] The candidate disposition is explicit: rollback, withdrawal, hold, or error.
- [ ] For rollback, the target names a **distinct prior release**.
- [ ] For withdrawal, no prior-release target is falsely supplied.
- [ ] For hold/error, no public mutation is implied.

### Evidence, policy, review, and correction

- [ ] Consequential claims have resolvable `EvidenceRef` → `EvidenceBundle` support or the correct outcome is `ABSTAIN`/withdrawal.
- [ ] Current policy references are known for a rollback candidate.
- [ ] Required review records are identified; their presence is not confused with completed review.
- [ ] If public notice is required, the correction-notice reference is present.
- [ ] Rights and sensitivity posture are evaluated under the **current** rules, not the historical release's rules alone.

### Agriculture-specific safety

- [ ] Field-, farm-, parcel-, operator-, well-, private-party-, and proprietary detail remains non-public unless explicitly authorized by current evidence and policy.
- [ ] A prior aggregate does not silently reintroduce more precise geometry than the current public-safe profile permits.
- [ ] Observation, model, classification, aggregate, forecast, and remotely sensed support roles remain distinct.
- [ ] Crop year, growing season, observation time, source time, release time, and correction time remain materially distinct where applicable.
- [ ] Cross-domain products such as soil, hydrology, atmosphere, habitat, or infrastructure remain linked through their owning authorities rather than copied into Agriculture truth.

### Downstream impact

- [ ] Dependent public and semi-public derivatives are enumerated.
- [ ] The recovery plan identifies which derivatives are invalidated, rebuilt, withdrawn, or left unchanged.
- [ ] The plan does not rely on deleting the failing release to hide stale dependents.

If a safety-critical precondition cannot be established, stop at `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` as appropriate.

[Back to top](#top)

---

## 7. Candidate decision and review

### 7.1 Build the RollbackCard candidate

Use the current shared release-family profile rather than the legacy minimal field list. The candidate must conform to:

- `contracts/release/rollback_card.md` for meaning;
- `schemas/contracts/v1/release/rollback_card.schema.json` for machine shape;
- `tools/validators/release/validate_rollback_card.py` for bounded candidate validation.

The current profile includes these top-level concepts:

| Concept | Role |
|---|---|
| Identity | `object_type`, `schema_version`, `id`, `version`, `spec_hash` |
| Disposition | rollback candidate, withdrawal candidate, hold, or error |
| Trigger | public-safe reason code and detection time |
| Affected release | immutable reference to the release under review |
| Target | prior release, withdrawal, or hold mode |
| Evidence / policy / review refs | separate support arrays |
| Correction notice | required when public notice is required |
| Invalidations | bounded invalidation classes |
| Restoration | intended restored release plus validation/notice posture |
| Timing | decision/effective times |
| Lineage | supersedes / superseded-by relationships |
| Governance | explicit non-authority flags and null release authority reference |

Do not duplicate the entire schema in this runbook. The schema and semantic contract are the authority for exact fields and finite values.

### 7.2 Validate the candidate locally

From repository root, the currently verified candidate validator can be invoked as:

```bash
python tools/validators/release/validate_rollback_card.py path/to/candidate.json
```

For the maintained fixture profile:

```bash
python tools/validators/release/validate_rollback_card.py --fixtures
```

A `PASS` means the candidate satisfies the current schema and local consistency rules. It does **not** resolve referenced releases, evidence, policy, signatures, actors, or approvals and does not execute rollback.

### 7.3 Required review burden

Review requirements are consequence-based, not merely defect-label-based. At minimum, require the owning accountable review path when recovery affects:

- rights or redistribution terms;
- sensitive or private Agriculture geometry/identity;
- source-role classification;
- evidence closure for a public claim;
- policy-significant exposure;
- public correction or withdrawal;
- any alias/current-state mutation;
- public AI or map behavior derived from the affected release.

Independent stewardship assignments remain `NEEDS VERIFICATION`; CODEOWNERS routing alone is not proof of independent approval.

[Back to top](#top)

---

## 8. Execution sequence

Execution begins only after the owning release, policy, evidence, and review authorities permit the intended transition. The exact mutation mechanism is owned outside this runbook.

1. **Freeze the affected release identity.** Record the immutable release reference and candidate evidence. Do not rewrite the original release.
2. **Contain unsafe exposure if required and authorized.** Use the current operational control plane; record what was disabled or held.
3. **Validate the RollbackCard candidate.** Candidate validation must pass or fail closed.
4. **Resolve referenced support.** Confirm the affected release, candidate target, evidence, policy, review, and correction references through their owning systems.
5. **Revalidate the target under current rules.** A historical release is not presumed safe.
6. **Choose one governed disposition.** Restore a verified prior release, withdraw without replacement, hold, or record error. Do not combine incompatible transitions.
7. **Perform the authorized release transition.** The current release authority owns the actual state mutation; this Markdown file does not.
8. **Issue correction/supersession records where required.** Publicly consequential changes must preserve visible correction lineage.
9. **Invalidate or rebuild downstream derivatives.** Use the bounded classes in [§9](#9-downstream-invalidation).
10. **Verify restored/withdrawn public-safe state.** Run the checklist in [§11](#11-post-rollback-verification).
11. **Preserve audit continuity.** Retain the failing release and associated receipts/proofs according to governing retention and correction policy.
12. **Record residual gaps.** Any unresolved consumer, stale derivative, ownership gap, or unverified operational control remains open rather than being hidden behind a successful candidate check.

> [!IMPORTANT]
> Recovery should prefer transparent supersession, withdrawal, or forward correction over shared-history rewriting or in-place mutation. A Git revert can undo repository bytes, but it does not by itself correct an already exposed public release.

[Back to top](#top)

---

## 9. Downstream invalidation

The current shared candidate profile recognizes these invalidation classes:

- `API_CACHE`
- `CDN`
- `TILES`
- `CATALOG`
- `TRIPLETS`
- `SEARCH_INDEX`
- `VECTOR_INDEX`
- `AI_CACHE`
- `DOWNSTREAM_DERIVATIVES`

Agriculture recovery planning should map each affected consumer into one or more of these classes, then resolve the actual tool or system responsible for invalidation.

### Agriculture examples

| Surface | Typical recovery action | Authority caution |
|---|---|---|
| Map tiles / PMTiles / other released carriers | Withdraw, replace, or rebuild from the verified target | Tiles are carriers, not truth |
| Catalog entry | Supersede or mark withdrawn/stale | Catalog presence is not release authority |
| Triplet/graph projection | Recompute or invalidate derived projection | Graph projection does not replace canonical evidence |
| Search/vector index | Rebuild from the current admissible corpus | Search results are not evidence authority |
| Governed API cache | Purge or version-bump according to runtime design | Do not expose internal release stores directly |
| Evidence Drawer payload | Show withdrawn/stale/corrected state based on governed response | UI state must reflect release/correction state |
| Focus Mode / AI cache | Invalidate answers that depended on the defective release | AI remains evidence-subordinate |
| Reports/exports | Reissue or withdraw with correction lineage | A static export can outlive a runtime rollback |

`DOWNSTREAM_DERIVATIVES` should be used when a dependent surface does not fit a narrower class. It is not permission to skip consumer inventory.

[Back to top](#top)

---

## 10. Agriculture-specific constraints

### 10.1 Rights and sensitive agricultural detail

Rollback must never restore a historical release merely because it is older if that release exposes:

- farm/operator identity;
- private parcel or field boundaries;
- proprietary yield or input records;
- private well or irrigation operation details;
- insurance, financial, or other private-party attributes;
- harmful precision introduced by joins with adjacent domains.

Where rights, privacy, or precision are unresolved, withdraw, quarantine, generalize, or hold rather than restore.

### 10.2 Source-role anti-collapse

Agriculture commonly combines heterogeneous support. Recovery must preserve the role of each source or derived product.

Examples:

- CDL or other classification is not ground observation merely because it is spatially precise.
- HLS/NDVI-derived stress signals are modeled/derived support, not direct farm truth.
- NASS aggregates do not become field-level observations.
- Weather, drought, or soil context does not become Agriculture-owned observation solely because it participates in a crop analysis.

If a prior release depended on a role collapse that current governance rejects, that release is not a valid rollback target.

### 10.3 Time and geography

Verify that the target matches the intended crop year, valid period, source vintage, release time, and spatial support. Do not repair a temporal defect by restoring a release with a different unacknowledged time basis.

Do not treat client-side masking or style visibility as a substitute for public-safe geometry transformation.

### 10.4 AI and map surfaces

A rollback affecting map or Focus Mode output must preserve the trust membrane:

```text
released/public-safe carrier or governed API
  -> evidence resolution + policy state
  -> map / Evidence Drawer / Focus Mode
```

Do not route public UI directly to RAW, WORK, QUARANTINE, internal release stores, or model providers during recovery.

[Back to top](#top)

---

## 11. Post-rollback verification

A recovery is not closed until its intended state and dependent surfaces are verified.

### Core verification

- [ ] The affected release remains auditable and immutable.
- [ ] The final disposition is recorded through the owning release/recovery authority.
- [ ] If a prior release was restored, its identity is distinct from the defective release and revalidated under current rules.
- [ ] Evidence, policy, review, correction, and restoration references resolve as required.
- [ ] Rights and sensitivity did not regress.
- [ ] Source roles remain intact.
- [ ] Time and spatial support match the intended public claim.
- [ ] Required correction/supersession lineage is visible.

### Downstream verification

- [ ] Every planned invalidation class has a verified outcome or an explicit open gap.
- [ ] Released map layers and downloads no longer reference the defective release where they should not.
- [ ] Catalog, search, graph/triplet, and vector projections are current or visibly stale/withdrawn.
- [ ] Governed API and UI trust states agree with release/correction state.
- [ ] Cached or generated AI answers dependent on the defective release are invalidated or no longer served as authoritative.

### Audit verification

- [ ] Original receipts, proofs, review records, manifests, and correction records are preserved according to retention rules.
- [ ] No audit artifact was deleted merely to make the recovery pass.
- [ ] The recovery itself has enough durable evidence to reconstruct who decided what, against which release, under which policy/evidence state.

If any required verification fails, leave the recovery on `HOLD` or escalate. Do not call the incident closed based solely on a green schema/validator result.

[Back to top](#top)

---

## 12. Finite outcomes and reason codes

### Candidate outcomes

The current shared RollbackCard profile uses:

| Candidate disposition | Meaning |
|---|---|
| `ROLLBACK_CANDIDATE` | Proposes restoration of a distinct prior release |
| `WITHDRAWAL_CANDIDATE` | Proposes withdrawal with no prior release selected |
| `HOLD` | Stops or delays recovery pending unresolved conditions |
| `ERROR` | Records invalid or failed recovery evaluation without public mutation |

Operational systems may expose additional bounded states such as `ABSTAIN` or `DENY` in policy/runtime envelopes, but do not silently rewrite the RollbackCard candidate vocabulary to include them.

### Shared trigger reason codes

The current validator/schema profile recognizes:

`RELEASE_DEFECT`, `EVIDENCE_CONTRADICTION`, `RIGHTS_CHANGE`, `SENSITIVITY_DISCOVERY`, `VALIDATION_FAILURE`, `SOURCE_WITHDRAWAL`, `POLICY_FAILURE`, `SECURITY_ISSUE`, `OPERATIONAL_FAILURE`, `EMERGENCY_HOLD`, `INSUFFICIENT_EVIDENCE`, `INPUT_INVALID`.

Use the narrowest accurate public-safe code. Sensitive details belong in appropriately protected review/incident evidence, not in a broadly visible reason field.

[Back to top](#top)

---

## 13. Drills and rehearsal

A rollback drill is valuable only when it proves deterministic, reversible behavior without mutating real public state.

### Current status

**HOLD / NEEDS VERIFICATION.** The Agriculture-specific drill lane currently documents the desired boundary but does not prove an executable end-to-end drill. Its repository-grounded README records:

- a documentation-only child lane at its inspected checkpoint;
- missing executable Agriculture rollback test implementation;
- TODO-only workflow behavior at that checkpoint;
- unresolved recovery topology and schema-home questions;
- unknown alias resolver, invalidation engine, release-state store, public UI/API stale-state integration, and production use.

The shared release-family candidate validator is stronger than that older drill description: the current shared contract/schema/validator/fixtures/tests are now present. That does **not** automatically graduate the Agriculture drill.

### Minimum credible Agriculture drill before graduation

A future substantive drill should prove, with synthetic no-network fixtures:

1. a defective release identity;
2. a distinct prior target and a withdrawal-with-no-target case;
3. evidence/policy/reference resolution using fixture-safe inputs;
4. non-regression of rights/sensitivity;
5. source-role preservation;
6. deterministic downstream invalidation planning;
7. public-state stale/withdrawn/restored projection without real publication;
8. audit preservation;
9. idempotent replay;
10. fail-closed behavior for missing/unsafe targets.

A passing drill would prove only that bounded synthetic recovery logic behaves as tested. Production authority and operational admission would remain separate.

[Back to top](#top)

---

## 14. Runbook change rollback

This documentation change is independently reversible from any operational Agriculture rollback.

### Before merge

Close or abandon the feature branch / draft PR. `main` remains unchanged.

### After merge

Use a transparent revert or forward-fix pull request against the actual merged commit. Do not rewrite shared history.

### Operational correction boundary

Reverting this Markdown file does **not** revert a release, source, public artifact, policy state, or correction record. Those state changes must be corrected through their owning release/lifecycle systems.

[Back to top](#top)

---

## 15. Anti-patterns

Never:

- silently replace released bytes in place;
- assume "older" means "safe";
- treat a valid RollbackCard as approval or execution;
- use schema validity as evidence resolution;
- delete the defective release or audit history to hide an incident;
- restore a release whose rights or sensitivity posture is weaker than current requirements;
- collapse classification, model, aggregate, forecast, or remotely sensed support into observation;
- hide sensitive geometry only with client styling;
- skip dependent caches, tiles, indexes, catalogs, triplets, exports, or AI caches because the main release pointer changed;
- use a runbook to create policy, review, release, or publication authority;
- present README-only drill design or TODO workflows as operational rollback readiness;
- invent a kill switch, alias mechanism, signer, validator, workflow, reviewer, or release route that current repository evidence does not prove.

[Back to top](#top)

---

## 16. Related surfaces

| Surface | Role |
|---|---|
| [`contracts/release/rollback_card.md`](../../../contracts/release/rollback_card.md) | Semantic meaning of the shared RollbackCard candidate |
| [`schemas/contracts/v1/release/rollback_card.schema.json`](../../../schemas/contracts/v1/release/rollback_card.schema.json) | Machine shape for the current candidate profile |
| [`tools/validators/release/validate_rollback_card.py`](../../../tools/validators/release/validate_rollback_card.py) | No-network candidate validator |
| [`tests/validators/test_validate_rollback_card.py`](../../../tests/validators/test_validate_rollback_card.py) | Focused validator tests |
| [`tests/domains/agriculture/rollback_drill/README.md`](../../../tests/domains/agriculture/rollback_drill/README.md) | Agriculture-specific desired drill boundary and current gaps |
| [`release/agriculture/README.md`](../../../release/agriculture/README.md) | Agriculture release-lane orientation; not superseded by this runbook |
| [`release/rollback_cards/README.md`](../../../release/rollback_cards/README.md) | Rollback-card review/record lane orientation |
| [`release/correction_notices/README.md`](../../../release/correction_notices/README.md) | Correction-notice lane orientation |
| [`release/manifests/README.md`](../../../release/manifests/README.md) | Release-manifest lane orientation |
| [`docs/runbooks/README.md`](../README.md) | Parent runbook boundary and maturity rules |
| [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) | Adopted placement doctrine through ADR-0029 |

[Back to top](#top)

---

## 17. Evidence basis

This revision is grounded in current repository evidence rather than the May 2026 scaffold assumptions in the prior runbook.

### CONFIRMED

- `docs/runbooks/agriculture/ROLLBACK_RUNBOOK.md` is an existing tracked runbook path under the `docs/` responsibility root.
- Accepted ADR-0029 adopts Directory Rules v2 and the parent runbook README identifies `docs/runbooks/` as the operational-procedure lane.
- The shared release-family `RollbackCard` semantic contract exists and defines a non-executing candidate plan.
- The paired `1.0.0` schema is closed and fixture-first.
- The no-network validator exists and checks bounded shape/local consistency.
- Focused validator tests cover positive/negative fixtures and fail-closed JSON/file handling.
- Candidate validation explicitly does not create authority, complete review/policy, execute rollback, mutate public state, or publish.
- The Agriculture rollback-drill README records that domain-specific executable drill readiness was not established at its repository-grounded checkpoint.

### NEEDS VERIFICATION

- Current accepted production rollback decision authority and independent stewardship.
- Exact production release-state mutation mechanism, alias/current-pointer semantics, invalidation engine, cache/CDN integration, public API/UI stale-state integration, signing, deployment, and operational drill evidence.
- Whether historical parallel Agriculture-specific rollback schema surfaces have since been formally retired or remain compatibility/drift surfaces.

### UNKNOWN

- Production rollback use, actual public release inventory, recovery SLOs, operator rotation, and live incident history unless established from current owning-system evidence.

### Non-effects

Updating this runbook changes documentation only. It does not:

- validate or execute a rollback;
- alter a contract, schema, validator, fixture, workflow, release manifest, RollbackCard, CorrectionNotice, receipt, proof, or policy;
- activate or deactivate a source;
- mutate `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLETS`, or `PUBLISHED` state;
- release, deploy, promote, or publish anything.

[Back to top](#top)
