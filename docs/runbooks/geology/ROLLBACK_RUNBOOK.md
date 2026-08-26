<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/geology/rollback-runbook
title: Geology and Natural Resources — Rollback, Withdrawal, and Recovery Runbook
type: runbook; operational-procedure; domain-lane; non-authoritative
version: v0.2
status: draft; repository-grounded; rollback-card-validator-present; synthetic-rehearsal-present; geology-release-held; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Geology, Natural Resources, release, rollback, correction, evidence, rights/sensitivity, source-role, and independent-review stewards"
created: 2026-05-12
updated: 2026-08-25
policy_label: public-review; geology; natural-resources; rollback; withdrawal; correction; fail-closed; no-publication-authority
current_path: docs/runbooks/geology/ROLLBACK_RUNBOOK.md
owning_root: docs/
responsibility: >
  Provide the repository-grounded human procedure for proposing, reviewing,
  rehearsing, executing through separately authorized machinery, verifying, and
  correcting a Geology and Natural Resources rollback or withdrawal without
  granting release, policy, evidence, review, deployment, or publication authority.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: same-path update; no new or parallel authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: a125b5b949627898f5a0b0f52a0a09f53b0c0483
  prior_blob: 0d7d404a13c5ae11d179dadd57e80d64c2a8f206
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  rollback_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  rollback_schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  rollback_validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  rollback_validator_test_blob: c8aeac6348127fb768981e2b5b5588c6a7bdeb78
  synthetic_rehearsal_blob: a8f6bff350e79b453f425ebce9a9ded6801f8944
  synthetic_rehearsal_test_blob: b644ca6c4185b3f81bc339c077eae85299833261
  geology_candidate_lane_blob: f0313cafc641c049d367af82418212e0bad1fc35
  geology_data_rollback_blob: f8baf132dc93dc51ff3d8a3687817d7e9cb66d43
  inspected_surfaces:
    - docs/runbooks/README.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/domains/geology/README.md
    - docs/domains/geology/SENSITIVITY.md
    - contracts/release/rollback_card.md
    - schemas/contracts/v1/release/rollback_card.schema.json
    - tools/validators/release/validate_rollback_card.py
    - tests/validators/test_validate_rollback_card.py
    - docs/runbooks/rollback-rehearsal.md
    - tools/release/rollback_apply.py
    - tests/release/test_synthetic_rollback_rehearsal.py
    - release/candidates/geology/README.md
    - release/rollback_cards/README.md
    - data/rollback/geology/README.md
    - tests/domains/geology/README.md
source_lineage:
  - "Connected Google Drive: KFM_Geology_Natural_Resources_Architecture_PDF_Only_Report_2026-04-21.pdf — planning lineage only; current repository evidence governs implementation claims"
related:
  - ../README.md
  - ../rollback-rehearsal.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/geology/README.md
  - ../../domains/geology/DATA_LIFECYCLE.md
  - ../../domains/geology/SENSITIVITY.md
  - ../../../contracts/release/rollback_card.md
  - ../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../tools/validators/release/validate_rollback_card.py
  - ../../../tests/validators/test_validate_rollback_card.py
  - ../../../tools/release/rollback_apply.py
  - ../../../tests/release/test_synthetic_rollback_rehearsal.py
  - ../../../release/candidates/geology/README.md
  - ../../../release/rollback_cards/README.md
  - ../../../release/correction_notices/README.md
  - ../../../release/manifests/README.md
  - ../../../data/rollback/geology/README.md
  - ../../../data/published/geology/README.md
  - ../../../tests/domains/geology/README.md
  - ../../../policy/domains/geology/README.md
tags: [kfm, geology, natural-resources, runbook, rollback, withdrawal, correction, release, source-role, public-safe-geometry, fail-closed]
notes:
  - "v0.2 replaces proposal-era paths, speculative CLI commands, stale field claims, and unbounded implementation statements with current repository evidence."
  - "The shared RollbackCard contract, closed 1.0.0 schema, fixture profile, no-network validator, and focused tests are present; candidate validation remains non-executing and non-authoritative."
  - "A marker-protected synthetic rollback/withdrawal helper and tests are present, but they prove only deterministic rehearsal behavior in an isolated synthetic workspace."
  - "The canonical Geology candidate lane contains only its README at the pinned revision; no child candidate dossier or tracked Geology-specific rollback drill was established by this inspection."
  - "This document changes no release record, alias, fixture, contract, schema, policy, validator, workflow, receipt, proof, lifecycle object, deployment, promotion, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology and Natural Resources — Rollback, Withdrawal, and Recovery Runbook

> **Recover a Geology public surface by resolving the affected release, current evidence, source role, rights, sensitivity, review, correction, invalidation, and rollback target—never by silently rewriting released bytes or assuming an older release is safe.**

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-state)
[![RollbackCard validator: present](https://img.shields.io/badge/RollbackCard%20validator-present-1f883d?style=flat-square)](#current-repository-state)
[![Synthetic rehearsal: present](https://img.shields.io/badge/synthetic%20rehearsal-present-1f883d?style=flat-square)](#current-repository-state)
[![Geology release path: HOLD](https://img.shields.io/badge/geology%20release%20path-HOLD-d4a72c?style=flat-square)](#current-repository-state)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-non-effects)

> [!IMPORTANT]
> **Rollback documentation is not rollback authority.** The shared release-family `RollbackCard` profile is implemented as a closed, fixture-first candidate schema with a no-network validator and focused tests. A passing card proves candidate shape and local consistency only. It does not approve rollback, execute policy, complete review, mutate an alias, invalidate a cache, issue a correction, release anything, or publish anything.

> [!CAUTION]
> **Synthetic rehearsal is not Geology operational readiness.** The repository includes a marker-protected, synthetic-only rollback/withdrawal helper and executable tests. The helper refuses non-synthetic scenarios and unmarked workspaces. Its report is rehearsal evidence, not a `RollbackCard`, `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`, release mutation, deployment, or publication record.

> [!WARNING]
> **An older target can still be unsafe.** Rights may have changed, exact subsurface detail may now require restriction, a source role or resource class may have been corrected, evidence may no longer resolve, map scale or vintage may be stale, or a sensitive join may now be prohibited. Revalidate the target under current governing rules before any recovery action.

**Quick navigation:** [Purpose](#1-purpose) · [Scope](#2-scope--non-goals) · [Placement](#3-repo-fit--placement) · [State](#current-repository-state) · [Authority](#authority-and-non-effects) · [Triggers](#6-trigger-classification-and-containment) · [Preconditions](#7-pre-rollback-preconditions) · [Candidate](#8-rollbackcard-candidate-and-review) · [Execution](#9-authorized-execution-sequence) · [Invalidation](#10-downstream-invalidation) · [Geology controls](#11-geology-specific-controls) · [Verification](#12-post-recovery-verification) · [Outcomes](#13-state-axes-outcomes-and-reason-codes) · [Drills](#14-drills-and-rehearsal) · [Runbook rollback](#15-rollback-of-this-runbook-change) · [Anti-patterns](#16-anti-patterns) · [Related](#17-related-surfaces) · [Evidence](#18-evidence-basis)

---

## 1. Purpose

This runbook defines the **human recovery procedure** for a Geology or Natural Resources release whose release-facing or public state is defective, unsafe, stale, unsupported, overclaimed, rights-conflicted, sensitivity-conflicted, or otherwise no longer admissible.

It answers six bounded questions:

1. When should the Geology lane propose rollback, withdrawal, hold, or a forward correction?
2. Which current repository objects and checks must resolve before action?
3. Which actions belong to release, correction, evidence, policy, review, data, cache, or delivery authorities rather than this Markdown file?
4. How do Geology-specific source roles, claim classes, exact subsurface detail, map scale, temporal vintage, and cross-lane joins affect recovery?
5. What can be rehearsed safely with the current synthetic helper?
6. What evidence is required before calling a recovery complete?

The governing pattern is:

```text
problem detected
  -> preserve evidence and contain unsafe exposure through authorized controls
  -> resolve affected release, current support, and current public state
  -> choose rollback candidate, withdrawal candidate, hold, error, or forward correction
  -> validate a RollbackCard candidate when rollback/withdrawal planning applies
  -> obtain required policy, rights, sensitivity, domain, review, correction, and release decisions
  -> act only through separately authorized release/delivery machinery
  -> invalidate or rebuild every affected derivative
  -> emit correction, supersession, withdrawal, and execution records where required
  -> verify public-safe state and audit continuity
  -/> silent mutation, hidden deletion, direct public-store editing, or documentation-as-authority
```

A runbook explains the procedure. It does not create the authority records or execute release state by prose alone.

[Back to top](#top)

---

## 2. Scope & non-goals

### In scope

- Recovery planning for a released or release-candidate Geology surface.
- `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, and `ERROR` candidate handling using the shared `RollbackCard` profile.
- Deciding when a separate forward correction is safer than rollback.
- Geology-specific source-role, resource-class, rights, sensitivity, temporal, scale, depth/vertical-reference, and public-safe-geometry checks.
- Downstream invalidation and re-derivation planning for tiles, catalogs, triplets, search/vector indexes, API/CDN state, AI caches, exports, reports, cross-sections, 3D/synthetic surfaces, and other dependent products.
- Correction, supersession, withdrawal, and stale-state obligations for previously exposed claims.
- Synthetic no-network rehearsal using current marker-protected tooling.
- Verification and audit-preservation requirements after an authorized recovery.

### Non-goals

- Approving rollback or acting as release authority.
- Treating a schema-valid `RollbackCard` as an approved or executed rollback.
- Treating a synthetic rehearsal report as a production release record.
- Choosing a new canonical schema, contract, policy, source-registry, release, or data home.
- Activating a source or connector.
- Writing directly to `PUBLISHED`, a current public alias, a CDN, a tile store, or an API cache from this runbook.
- Deleting a failing release, receipt, proof, correction record, source capture, or audit trail to make recovery appear clean.
- Replacing required human, rights-holder, sensitivity, domain, policy-significant, or independent review.
- Certifying mineral reserves, extraction feasibility, engineering safety, title, mineral rights, regulatory compliance, or legal ownership.
- Claiming that Geology public aliases, production invalidators, release signing, deployment, or production rollback are implemented when current evidence does not establish them.

[Back to top](#top)

---

## 3. Repo fit & placement

**Placement outcome: `PLACE` — CONFIRMED for this same-path update.**

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). The parent [`docs/runbooks/` index](../README.md) identifies `docs/runbooks/` as the operational-procedure lane under the `docs/` responsibility root. The target is an existing tracked Geology runbook and this revision does not create, move, rename, split, mirror, or delete an authority surface.

| Property | Current result |
|---|---|
| Path | `docs/runbooks/geology/ROLLBACK_RUNBOOK.md` |
| Authority owner | `docs/` — human-facing operational procedure |
| Scope | Geology and Natural Resources domain lane |
| Path state | Existing tracked path; same-path modernization |
| Structural effect | None |
| Review route | `@bartytime4life` through repository review routing |
| Independent stewardship | `NEEDS VERIFICATION` |
| Release/publication effect | None |

This file may cite contracts, schemas, validators, fixtures, release records, evidence, policy, review, correction, recovery tools, and data-plane support. It cannot replace any of them.

[Back to top](#top)

---

<a id="current-repository-state"></a>

## 4. Current repository state

The following observations are pinned to `main@a125b5b949627898f5a0b0f52a0a09f53b0c0483`. They describe repository bytes and bounded test surfaces, not deployed behavior.

| Surface | CONFIRMED current evidence | Bounded conclusion |
|---|---|---|
| Prior Geology rollback runbook | Tracked blob `0d7d404a...`; proposal-era paths, fields, commands, and repo-unknown language remained | Same-path repository-grounded correction is warranted |
| Directory governance | Accepted ADR-0029 adopts the exact Directory Rules blob `fd49a0b...` | This tracked runbook remains in the correct responsibility root |
| Shared RollbackCard contract | [`contracts/release/rollback_card.md`](../../../contracts/release/rollback_card.md) defines candidate semantics and non-authority boundaries | Shared release-family meaning exists |
| Shared RollbackCard schema | [`rollback_card.schema.json`](../../../schemas/contracts/v1/release/rollback_card.schema.json) is closed, version `1.0.0`, and fixture-first | Candidate machine shape is defined |
| Shared RollbackCard validator | [`validate_rollback_card.py`](../../../tools/validators/release/validate_rollback_card.py) performs no-network schema and local-consistency checks | Candidate validation is executable and bounded |
| Focused validator tests | [`test_validate_rollback_card.py`](../../../tests/validators/test_validate_rollback_card.py) checks schema validity, positive/negative fixtures, CLI profile, duplicate keys, non-finite numbers, and missing files | The candidate validator has focused executable coverage |
| Shared synthetic rehearsal | [`rollback_apply.py`](../../../tools/release/rollback_apply.py) requires a marker-protected root and `synthetic: true`; plan mode is default | Cross-domain rehearsal mechanics exist only for synthetic workspaces |
| Synthetic rehearsal tests | [`test_synthetic_rollback_rehearsal.py`](../../../tests/release/test_synthetic_rollback_rehearsal.py) checks deterministic planning, rollback, withdrawal, history preservation, complete invalidation, and fail-closed inputs | Synthetic rollback behavior has executable coverage |
| Geology candidate lane | `release/candidates/geology/` contains only its README at the pinned revision | No child Geology candidate dossier is established in the canonical candidate lane |
| Geology rollback data lane | [`data/rollback/geology/README.md`](../../../data/rollback/geology/README.md) documents data-plane support and exact-detail boundaries | Path guidance exists; it is not release authority and proves no rollback instance |
| Geology-specific rollback drill | No tracked `tests/domains/geology/rollback_drill/README.md` was found by direct path check | A Geology-specific rollback drill artifact is not established |
| Geology domain tests | [`tests/domains/geology/README.md`](../../../tests/domains/geology/README.md) records two bounded executable fixture suites and broader release integration as incomplete | Domain test depth exists but does not prove rollback graduation |
| Public alias, production invalidation, signing, deployment, operational release | Not established by the inspected surfaces | `UNKNOWN` / `NEEDS VERIFICATION`; do not invent commands or claim readiness |

### Current safe determination

- **CONFIRMED:** candidate validation and synthetic rehearsal mechanics exist.
- **CONFIRMED:** the canonical Geology candidate lane has no child candidate dossier at this checkpoint.
- **CONFIRMED:** the Geology data-plane rollback README does not prove a rollback instance.
- **NEEDS VERIFICATION:** accountable operational owners, executable Geology rollback drill, live alias resolver, cache invalidators, signer custody, deployment integration, and production recovery evidence.
- **HOLD:** any claim that Geology rollback is operationally admitted or production-ready.
- **UNKNOWN:** releases, aliases, or runtime state outside the bounded repository surfaces inspected here.

[Back to top](#top)

---

<a id="authority-and-non-effects"></a>

## 5. Authority and non-effects

Rollback crosses several responsibility roots. Keep each authority separate.

| Concern | Owning surface | This runbook's role |
|---|---|---|
| Rollback candidate meaning | [`contracts/release/rollback_card.md`](../../../contracts/release/rollback_card.md) | Explain and link; do not redefine |
| Candidate machine shape | [`schemas/contracts/v1/release/rollback_card.schema.json`](../../../schemas/contracts/v1/release/rollback_card.schema.json) | Cite exact required fields and vocabularies |
| Candidate validation | [`tools/validators/release/validate_rollback_card.py`](../../../tools/validators/release/validate_rollback_card.py) | Provide verified command and interpret its bounded result |
| Policy outcome | `policy/` plus accountable review | Require resolution; do not create `ALLOW`, `DENY`, or other decisions |
| Evidence support | EvidenceRef/EvidenceBundle and proof authorities | Require resolution; do not turn prose into evidence |
| Human review | ReviewRecord and accountable reviewer routes | Assemble a review packet; do not self-approve |
| Release decision and public mutation | `release/` plus admitted execution machinery | Describe sequence; do not execute from Markdown |
| Correction/withdrawal notice | Correction and release notice authorities | Require public lineage where claims changed |
| Data-plane rollback support | [`data/rollback/geology/`](../../../data/rollback/geology/README.md) | Point to support records; do not place release authority there |
| Synthetic rehearsal | [`tools/release/rollback_apply.py`](../../../tools/release/rollback_apply.py) and tests | Exercise isolated mechanics only |
| Public UI/API/map/AI behavior | Governed delivery surfaces | Verify results; never write internal state directly |

This runbook has **no effect** on:

- source admission or source activation;
- evidence truth or citation resolution;
- policy, rights, sensitivity, or review decisions;
- release state, public aliases, caches, tiles, catalogs, indexes, or deployments;
- correction, withdrawal, supersession, or rollback execution;
- publication or removal of public material;
- schema, contract, validator, workflow, or repository settings.

[Back to top](#top)

---

## 6. Trigger classification and containment

### 6.1 Choose the recovery posture

Use the smallest safe recovery that closes the defect without hiding history.

| Posture | Use when | Required target posture | Public-state implication |
|---|---|---|---|
| **Forward correction** | Current release can remain safely available while a bounded claim or artifact is corrected through a new governed record | Current release support remains admissible; correction scope is complete | Preserve current release until the correction/superseding release is authorized |
| **`ROLLBACK_CANDIDATE`** | An affected release is unsafe or defective and a distinct prior release may be restored | Prior release must be revalidated under current rules | Candidate only until separate policy, review, correction, release, and execution authority close |
| **`WITHDRAWAL_CANDIDATE`** | Exposure must stop and no prior release is safe or appropriate | No target release | Candidate only; withdrawal must remain visible and auditable |
| **`HOLD`** | Evidence, target, rights, sensitivity, ownership, review, or execution authority is unresolved | No public mutation | Preserve current governed state or apply separately authorized containment |
| **`ERROR`** | Input, candidate, tooling, identity, or support is invalid | No public mutation | Record the failure safely and escalate |

Do not select rollback merely because it is faster. Rollback is appropriate only when a distinct target can be shown safer than the affected state.

### 6.2 Recognized RollbackCard trigger reason codes

The current schema permits:

- `RELEASE_DEFECT`
- `EVIDENCE_CONTRADICTION`
- `RIGHTS_CHANGE`
- `SENSITIVITY_DISCOVERY`
- `VALIDATION_FAILURE`
- `SOURCE_WITHDRAWAL`
- `POLICY_FAILURE`
- `SECURITY_ISSUE`
- `OPERATIONAL_FAILURE`
- `EMERGENCY_HOLD`
- `INSUFFICIENT_EVIDENCE`
- `INPUT_INVALID`

Use a public-safe classification. Do not place exact restricted coordinates, exploit detail, private-well identity, proprietary source content, or unredacted reviewer text in the trigger.

### 6.3 Immediate containment

Containment must use an already authorized control. This runbook does not authorize one.

1. **Open a stable incident/change identity.** Record detector, time, affected public scope, and public-safe reason.
2. **Preserve state.** Freeze affected release bytes, manifests, source captures, evidence, logs, receipts, reviews, and public observations needed for reconstruction.
3. **Stop new promotion.** Hold dependent candidate or release work while the defect is evaluated.
4. **Restrict harmful precision.** When exact subsurface, private-well, well-log, core/sample, resource, infrastructure, or proprietary detail may be exposed, fail closed through an authorized deny, restriction, withdrawal, or stale-state mechanism.
5. **Record current exposure.** Capture which API routes, tiles, catalogs, indexes, reports, exports, map states, Evidence Drawer payloads, and AI surfaces currently expose or depend on the affected release.
6. **Notify accountable roles.** At minimum: release, Geology domain, evidence, policy, correction, and rights/sensitivity stewards appropriate to consequence.
7. **Do not mutate history.** No deletion, overwrite, force-update, direct canonical-store edit, or unrecorded alias switch.

When containment capability or authority is unclear, return `HOLD` or `ESCALATE`; do not improvise a public mutation.

[Back to top](#top)

---

## 7. Pre-rollback preconditions

All applicable checks must close before an operational rollback or withdrawal. A validated candidate is necessary but not sufficient.

### 7.1 Identity and release binding

- [ ] `affected_release_ref` resolves to the exact release under review.
- [ ] The affected release identity, manifest, artifact inventory, and digests are frozen.
- [ ] A rollback target is a **distinct** prior release; it is not the affected release renamed.
- [ ] For withdrawal, target release fields are `null` as required by the schema.
- [ ] The target's artifacts and manifest digests match retained bytes.
- [ ] Scope, geography, map edition, temporal vintage, scale/resolution, depth/vertical reference, and source roles are known for affected and target releases.
- [ ] Concurrent release or correction work is frozen or reconciled so a stale decision cannot overwrite newer state.

### 7.2 Evidence, source, and claim support

- [ ] Every consequential restored claim resolves through admissible EvidenceRef/EvidenceBundle support.
- [ ] SourceDescriptor state, source role, rights, terms, cadence, and withdrawal/stale state are current.
- [ ] Occurrence, deposit, estimate, permit, production, reserve, observation, interpretation, model, aggregate, regulatory, administrative, contextual, and synthetic roles remain distinct.
- [ ] A prior generalized map, model surface, cross-section, tile, report, catalog record, graph edge, or AI summary is not treated as sovereign evidence.
- [ ] Evidence contradictions are represented and reviewed rather than removed from history.

### 7.3 Rights, sensitivity, and public-safe geometry

- [ ] Current rights and source terms permit the target's intended use.
- [ ] Exact or reverse-engineerable borehole, private-well, well-log, core/sample, geophysics, geochemistry, mineral/resource, extraction, reclamation, and infrastructure-sensitive detail has an explicit disposition.
- [ ] Any generalization, aggregation, redaction, withholding, or denial is supported by the required transform/review records.
- [ ] Sensitive joins are evaluated at the output level, including parcel/operator, well/private property, resource/extraction, archaeology, or infrastructure combinations.
- [ ] Rollback artifacts and notices do not leak redaction offsets, generalization radii, transform parameters, or other reverse-engineering aids.

### 7.4 Policy, review, correction, and authority

- [ ] Required policy decisions resolve for both affected and target states.
- [ ] Required Geology, release, evidence, rights, sensitivity, correction, and independent reviews are assigned and complete.
- [ ] Separation of duties is satisfied for the consequence level.
- [ ] Public-notice requirements are known.
- [ ] `correction_notice_ref` is present when `public_notice_required` is true.
- [ ] The operator has verified authority for the named environment and action.
- [ ] Signer identity, key custody, release locking, and audit capture are established where required.
- [ ] The execution path is separately admitted; a guessed CLI or manual file move is prohibited.

### 7.5 Invalidation and recovery closure

- [ ] Every affected derivative class is inventoried.
- [ ] Owners and mechanisms exist for required cache/index/tile/catalog/AI invalidations.
- [ ] Rebuild inputs point to the authorized target, not the affected release.
- [ ] A post-recovery verification plan has pass/fail criteria.
- [ ] A stop/abort path exists before public mutation.
- [ ] A follow-forward plan exists if the target also fails validation.
- [ ] Audit and correction lineage will remain inspectable.

Any unresolved mandatory item yields `HOLD`, `DENY`, `ERROR`, or `ESCALATE` as appropriate. It never yields implicit approval.

[Back to top](#top)

---

## 8. RollbackCard candidate and review

### 8.1 Current schema-paired field surface

Every schema-valid candidate contains:

| Field | Purpose |
|---|---|
| `object_type` | Constant `RollbackCard` |
| `schema_version` | Constant `1.0.0` |
| `id` | Stable candidate identity |
| `version` | Candidate semantic version |
| `spec_hash` | Non-placeholder `sha256:` binding |
| `disposition` | `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, or `ERROR` |
| `trigger` | Public-safe reason code and timezone-aware detection time |
| `affected_release_ref` | Exact affected release |
| `target` | `PRIOR_RELEASE`, `WITHDRAWAL`, or `HOLD` plus release reference rules |
| `evidence_bundle_refs` | Sorted, unique candidate support references |
| `policy_decision_refs` | Sorted, unique policy references |
| `review_record_refs` | Sorted, unique review references |
| `correction_notice_ref` | Correction/notice reference or `null` |
| `invalidations` | One or more finite invalidation classes |
| `restoration` | Intended restored release, notice requirement, validation requirement |
| `timing` | Decision and optional effective times |
| `lineage` | Supersession references |
| `governance` | Explicit candidate-only non-authority state |

The validator also checks disposition/target consistency, distinct target release, required evidence and policy references for rollback candidates, restoration-target consistency, notice linkage, time ordering, canonical arrays, non-self-supersession, and the governance boundary.

### 8.2 Candidate governance boundary

The fixture-first schema requires these fields to remain false:

```json
{
  "authority_created": false,
  "policy_evaluated": false,
  "review_completed": false,
  "rollback_executed": false,
  "public_state_mutated": false,
  "release_ref": null
}
```

Do **not** flip these values to represent production progress. The current profile is intentionally non-executing. Accepted decisions, reviews, execution receipts, correction records, release manifests, and public-state evidence remain separate object families.

### 8.3 Validate the candidate

Repository-native focused commands:

```bash
python tools/validators/release/validate_rollback_card.py --fixtures

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
```

To validate one or more candidate files:

```bash
python tools/validators/release/validate_rollback_card.py \
  <candidate-one.json> \
  <candidate-two.json>
```

Interpretation:

| Result | Meaning | Does not mean |
|---|---|---|
| `PASS` | Candidate matches the closed schema and local semantic checks | References resolve, target is safe, policy passed, review completed, execution occurred, or public state changed |
| `FAIL` | Candidate is malformed or locally inconsistent | The underlying incident is false or no recovery is needed |
| Tool/file error | Input or validator could not be evaluated safely | Permission to bypass validation |

### 8.4 Review packet

A review packet should contain only public-safe or access-appropriate material and should bind:

- exact candidate ID, version, and digest;
- affected and target release identities and manifest digests;
- public-safe defect summary and trigger reason;
- affected claim classes, object families, geography, time, map edition, scale, depth/vertical reference, and delivery surfaces;
- evidence, source, rights, sensitivity, policy, and review references;
- difference between affected and target releases;
- source-role and resource-class comparison;
- sensitive-geometry and transform comparison;
- complete invalidation plan;
- correction, withdrawal, supersession, and notice obligations;
- execution owner, environment, lock/concurrency plan, stop conditions, and rollback-of-rollback posture;
- post-recovery acceptance checks;
- open unknowns and explicit `HOLD` conditions.

A review packet does not become approval by completeness alone.

[Back to top](#top)

---

## 9. Authorized execution sequence

> [!IMPORTANT]
> **No production rollback command is standardized by this runbook.** Current repository evidence establishes a candidate validator and a synthetic-only helper. Production alias mutation, cache invalidation, signing, deployment, and release orchestration remain `NEEDS VERIFICATION`. Execute only through a separately reviewed and admitted mechanism for the named environment.

### Phase A — freeze and verify

1. Freeze the exact affected release, target release, candidate, decisions, and support digests.
2. Verify the public state still matches the decision basis.
3. Verify no newer correction, promotion, supersession, or incident owns the same release scope.
4. Re-run target validation under current contracts, policy, rights, sensitivity, source-role, and evidence rules.
5. Reconcile any mismatch before public mutation.

**Stop conditions:** identity mismatch, digest mismatch, target equals affected release, stale support, unresolved rights/sensitivity, missing evidence, missing reviewer, concurrent owner, or incomplete invalidation.

### Phase B — authorize

1. Resolve required policy decisions.
2. Complete required domain, release, evidence, rights/sensitivity, correction, and independent reviews.
3. Confirm public notice and correction requirements.
4. Confirm the separately admitted executor, credentials, signer, environment, and audit destination.
5. Record the authorized effective time and abort window.

**Stop conditions:** authority unknown, policy not resolved, review incomplete, signer or environment unverified, or execution path not admitted.

### Phase C — apply through owning machinery

Depending on the authorized decision, owning release/delivery machinery should:

- restore a distinct prior release;
- withdraw the affected release without choosing a target;
- preserve the affected release as retained history;
- emit or link required correction/withdrawal/supersession records;
- update only governed release pointers or delivery state;
- emit execution and alias-revert receipts through their owning families;
- prevent partial public state from being treated as success.

The documentation author must not simulate this phase by moving files, editing `data/published/` directly, changing a README, or inventing a CLI.

### Phase D — invalidate and rebuild

1. Invalidate every affected delivery and derived surface.
2. Rebuild only from the authorized target and current public-safe transforms.
3. Re-run evidence, policy, rights, sensitivity, source-role, catalog, and public-interface checks.
4. Keep affected release bytes, manifests, proofs, receipts, and review history immutable and inspectable.

### Phase E — verify and close

1. Execute the post-recovery checklist in §12.
2. Compare expected and observed public state.
3. Record unresolved propagation or stale-state issues.
4. Keep the recovery open until every required surface is confirmed or explicitly held.
5. Emit closure evidence through the owning audit/receipt/review families.
6. Schedule follow-up correction, source refresh, or forward release work where needed.

A partial alias switch with stale tiles, indexes, caches, or AI responses is not a complete rollback.

[Back to top](#top)

---

## 10. Downstream invalidation

The `RollbackCard` schema permits the following finite classes. Include every class actually affected. The synthetic rehearsal profile is stricter and requires the complete set.

| Invalidation class | Geology examples | Verification |
|---|---|---|
| `API_CACHE` | Geology feature, evidence, catalog, search, cross-section, or Focus payloads | Requests no longer resolve the affected release as current |
| `CDN` | Static published carriers, manifests, sidecars, exports, reports | Purge/expiry evidence matches affected digests and keys |
| `TILES` | PMTiles, MVT, raster tiles, terrain/3D delivery, map source caches | Tile metadata and sampled requests bind the authorized target |
| `CATALOG` | Domain catalog, STAC/DCAT-style projections, layer registries | Current catalog references authorized release and correction lineage |
| `TRIPLETS` | Geology/resource graph or triplet projections | Affected release edges are stale/superseded and rebuilt from target |
| `SEARCH_INDEX` | Text, faceted, spatial, or layer search | Search results do not surface affected release as current |
| `VECTOR_INDEX` | Retrieval or semantic indexes used by governed AI/search | Affected chunks are removed or stale and target chunks are rebuilt |
| `AI_CACHE` | Focus Mode, summaries, explanation caches, citation payloads | Responses resolve current EvidenceBundle and release state |
| `DOWNSTREAM_DERIVATIVES` | Reports, exports, story nodes, screenshots, previews, dashboards, cross-sections, 3D/synthetic surfaces | Dependency inventory is complete and each carrier is rebuilt, withdrawn, or marked stale |

### Invalidation rules

- The RollbackCard schema requires at least one invalidation class and canonical ordering for a populated array.
- The synthetic rehearsal helper requires all nine classes so the cross-domain rehearsal cannot silently skip a carrier family.
- An operational recovery should list every affected class, but must not claim unaffected systems merely to satisfy a checklist.
- Detailed keys, artifact IDs, purge targets, and rebuild receipts belong in scoped execution/invalidation records, not in the public trigger summary.
- Do not store credentials, restricted coordinates, private source identifiers, or reverse-engineering detail in public invalidation records.
- If any affected derivative cannot be invalidated or made visibly stale, keep recovery at `HOLD` or `ERROR`; do not call it complete.

[Back to top](#top)

---

## 11. Geology-specific controls

### 11.1 Source-role and resource-class anti-collapse

A rollback must preserve the strength and meaning of each claim. Never use recovery to upgrade or blur:

```text
Occurrence != Deposit != Estimate != Permit != Production != Reserve
Observation != Interpretation != Model != Aggregate != Synthetic surface
Administrative/regulatory record != physical geology
Generalized map carrier != exact source evidence
```

Examples:

- A permit or lease does not prove a deposit.
- Production history does not prove a current reserve.
- A modeled resource-potential surface does not become a confirmed occurrence.
- A historical geologic map does not become current field observation.
- An AI summary or map popup does not become evidence.
- A catalog record proves discoverability and linkage, not claim truth.
- A prior release's terminology does not override a newer corrected source-role decision.

If the target release collapses roles that current rules separate, deny the rollback target and use withdrawal or forward correction.

### 11.2 Exact subsurface and harmful precision

Fail closed for exact or reverse-engineerable:

- boreholes and private wells;
- well logs and rights-controlled log content;
- core and sample coordinates;
- geophysics and geochemistry points or fine grids;
- mineral occurrences, deposits, estimates, and extraction-targetable detail;
- extraction and reclamation sites when public exposure creates risk;
- infrastructure-sensitive subsurface context;
- proprietary or rights-unclear data.

A previously public exact location does not remain safe merely because it was once released. Reapply current public-safe geometry, rights, sensitivity, and review rules to the target.

### 11.3 Sensitive joins

Evaluate the joined output, not each input alone. Hold or deny joins that can reveal:

- borehole/private-well location × parcel or owner;
- operator × extraction site × parcel;
- occurrence cluster × precise coordinates;
- rights-controlled log content × public reproduction;
- geochemistry anomaly × fine spatial grid;
- geology × archaeology or critical infrastructure;
- generalized public feature × internal identifier that enables re-identification.

A T0/public input joined to another public input can produce a restricted result.

### 11.4 Time, map edition, scale, and vertical context

Before restoring a target, compare:

- source publication and retrieval time;
- observation/valid time;
- correction and effective time;
- geologic map edition or boundary version;
- map scale and intended use;
- coordinate reference system;
- elevation/depth datum and vertical reference;
- model or interpretation version;
- source withdrawal or stale state.

Do not restore a coarse regional map as if it supported site-scale claims. Do not combine incompatible depth datums or vintages without an explicit transform and uncertainty record.

### 11.5 Cross-lane boundaries

Rollback must not overwrite adjacent-domain authority:

| Relation | Boundary |
|---|---|
| Geology ↔ Hydrology | Hydrostratigraphic context may relate to water systems; Geology does not own hydrologic measurements or water-right decisions |
| Geology ↔ Hazards | Geology owns structures and earth-material context; Hazards owns risk/warning interpretation |
| Geology ↔ Soil | Geology may supply parent-material context; Soil owns soil observations and mapunit truth |
| Geology ↔ People/Land | Parcel, title, lease, mineral-right, and ownership assertions do not become physical geology |
| Geology ↔ Archaeology | Sensitive cultural-location controls remain independent and may be stricter |
| Geology ↔ Infrastructure | Public-safety and critical-infrastructure precision must remain governed by the owning lane |

### 11.6 Representations, cross-sections, and 3D

Cross-sections, interpolations, generalized surfaces, terrain, point clouds, 3D scenes, and digital-twin-like products are representations. When a target restores one:

- preserve source data and interpretation distinction;
- carry uncertainty and reality-boundary notes where material;
- verify the 2D/evidence baseline remains available;
- do not infer subsurface volume or continuity beyond support;
- invalidate rendered carriers and derived screenshots separately from canonical evidence.

### 11.7 Public API, map, Evidence Drawer, and AI

After recovery:

- public clients use governed interfaces and released public-safe carriers only;
- map features identify candidates, not truth authority;
- EvidenceRef resolves to EvidenceBundle before consequential claims;
- AI may interpret the authorized released evidence but cannot select, approve, or execute rollback;
- cached answers tied to the affected release are invalidated;
- unresolved support yields `ABSTAIN`, `DENY`, or `ERROR`, not a fluent guess.

[Back to top](#top)

---

## 12. Post-recovery verification

Do not close recovery until all applicable checks pass or are recorded as an explicit hold.

### 12.1 Release and artifact state

- [ ] The observed release-facing state matches the authorized rollback or withdrawal outcome.
- [ ] The affected release is no longer presented as current where it should not be.
- [ ] The restored release is the exact approved target.
- [ ] Target manifest and artifact digests match retained bytes.
- [ ] Affected release bytes and history remain immutable and inspectable.
- [ ] Correction, withdrawal, supersession, and lineage references resolve.
- [ ] Any required public notice is present and public-safe.

### 12.2 Evidence, policy, rights, and sensitivity

- [ ] Every restored consequential claim resolves to current admissible evidence.
- [ ] Source roles and resource classes are preserved.
- [ ] Rights and source terms are current.
- [ ] Sensitivity decisions and public-safe geometry transforms are current.
- [ ] No exact or reverse-engineerable protected detail is exposed.
- [ ] Required domain, release, evidence, rights/sensitivity, correction, and independent reviews are recorded.
- [ ] Policy outcomes are consistent with the restored public state.

### 12.3 Delivery and derivatives

- [ ] Every required invalidation class is complete.
- [ ] API/CDN/tile/catalog/triplet/search/vector/AI/downstream state resolves to the target or an explicit withdrawn/stale state.
- [ ] Map layer metadata, legends, popups, Evidence Drawer payloads, exports, reports, cross-sections, and 3D/synthetic surfaces show correct release and correction lineage.
- [ ] No stale target from the affected release remains current in deep links, bookmarks, caches, or indexes.
- [ ] Regenerated derivatives were built from authorized inputs and have current digests.

### 12.4 Runtime and user-visible behavior

- [ ] Public requests produce the intended finite outcome.
- [ ] Unresolved evidence produces `ABSTAIN`; prohibited exposure produces `DENY`; system failure produces `ERROR`.
- [ ] A withdrawn or superseded release is visible as such rather than disappearing without history.
- [ ] Citations and evidence links point to the authorized release.
- [ ] Monitoring shows no continuing requests for affected release identifiers beyond expected stale-client behavior.
- [ ] Any residual propagation delay is documented and does not expose unsafe content.

### 12.5 Audit and closure

- [ ] Candidate, decisions, reviews, notices, execution evidence, invalidation records, and verification evidence are linked.
- [ ] Detection, decision, effective, correction, and transaction times are preserved.
- [ ] The incident/change record states what remains unknown.
- [ ] Follow-forward work has an owner and rollback target.
- [ ] Recovery is not called complete solely because one alias, command, workflow, or UI check passed.

[Back to top](#top)

---

## 13. State axes, outcomes, and reason codes

Do not collapse candidate, procedure, runtime, release, and publication states.

| Axis | Finite values used here | Meaning |
|---|---|---|
| RollbackCard disposition | `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, `ERROR` | Candidate planning result |
| Target mode | `PRIOR_RELEASE`, `WITHDRAWAL`, `HOLD` | Candidate target shape |
| Procedure result | `PASS`, `HOLD`, `DENY`, `ERROR`, `ESCALATE` | Human runbook checkpoint result; not a schema or release state |
| Runtime response | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Governed outward response |
| Release state | Defined by the current release authority and manifest profile | Must be read from the owning release object, not inferred here |
| Publication state | Actual governed exposure of a public-safe carrier | Separate from merge, validation, candidate, review, and release paperwork |

### Procedure result meanings

| Result | Meaning |
|---|---|
| `PASS` | The named checkpoint's bounded conditions were verified |
| `HOLD` | Required information, authority, target, review, or capability is unresolved |
| `DENY` | Current rules prohibit the requested action or target |
| `ERROR` | Validation, identity, digest, tooling, execution, or verification failed |
| `ESCALATE` | A named steward, rights-holder, security, sensitivity, release, or independent-review decision is required |

A `PASS` at candidate validation is not a release approval. A `PASS` in synthetic rehearsal is not production readiness. A public `ANSWER` is not proof that rollback executed correctly unless it resolves to the authorized release and evidence.

[Back to top](#top)

---

## 14. Drills and rehearsal

### 14.1 Current shared synthetic rehearsal

The repository provides a deterministic, no-network rehearsal:

```bash
python -m unittest -q tests.release.test_synthetic_rollback_rehearsal
```

The helper defaults to a no-write plan:

```bash
python tools/release/rollback_apply.py \
  --workspace /tmp/kfm-rehearsal \
  --scenario /tmp/kfm-rehearsal/scenario.json
```

`--apply` still changes only a marker-protected synthetic workspace:

```bash
python tools/release/rollback_apply.py \
  --workspace /tmp/kfm-rehearsal \
  --scenario /tmp/kfm-rehearsal/scenario.json \
  --apply
```

Required synthetic safeguards:

- workspace contains `.kfm-synthetic-rollback-rehearsal` with exact content `synthetic-only`;
- scenario contains `synthetic: true`;
- operation is `ROLLBACK` or `WITHDRAWAL`;
- affected and target identities and expected digests are explicit;
- all nine invalidation classes are present;
- correction identity, reason, and decision time are present;
- affected release bytes remain unchanged;
- report governance fields remain non-authoritative.

### 14.2 What the rehearsal proves

A passing test can prove, for bounded synthetic fixtures:

- deterministic plan output;
- target and artifact digest verification;
- rollback to a distinct prior release;
- withdrawal without a target;
- complete invalidation inventory;
- correction and invalidation record creation inside the synthetic root;
- preservation of affected release bytes;
- denial of non-synthetic or unsafe inputs.

It does not prove:

- a Geology candidate exists;
- a Geology release or public alias exists;
- current rights, sensitivity, source-role, evidence, or policy resolution;
- production cache/CDN/tile/index invalidation;
- signer custody, deployment, or live rollback;
- release or publication authority.

### 14.3 Requirements for a Geology-specific drill

A future Geology drill should remain a separate, dependency-closed implementation slice and should add:

- synthetic/public-safe Geology affected and prior releases;
- a schema-valid candidate RollbackCard;
- Geology source-role and resource-class anti-collapse checks;
- exact borehole/private-well/resource-location leakage negatives;
- rights and sensitivity change scenarios;
- map edition, time, scale, CRS, and vertical-reference mismatch negatives;
- public-safe geometry transform and citation checks;
- API/tile/catalog/search/vector/AI invalidation verification;
- correction, withdrawal, supersession, and stale-state behavior;
- no-network execution and marker-protected writes;
- tests that distinguish candidate validation, rehearsal, review, release, and publication.

Until that slice exists and is reviewed, Geology rollback rehearsal remains `HOLD` beyond the shared synthetic mechanics.

[Back to top](#top)

---

## 15. Rollback of this runbook change

This revision is documentation-only and same-path.

To reverse it:

1. Revert the feature-branch commit that replaces this file, or restore prior blob `0d7d404a13c5ae11d179dadd57e80d64c2a8f206` in a reviewed follow-up.
2. Re-run documentation/link checks applicable to the repository.
3. Record why the current repository-grounded procedure was withdrawn or superseded.
4. Do not treat document rollback as release rollback.

Reverting this file changes no release record, public alias, candidate, policy decision, EvidenceBundle, cache, catalog, artifact, deployment, or publication state.

[Back to top](#top)

---

## 16. Anti-patterns

Refuse each of the following:

- **Silent file replacement:** overwriting published bytes without correction or lineage.
- **Alias-only success:** declaring rollback complete after changing one pointer while derivatives remain stale.
- **Older-is-safe assumption:** restoring a prior release without current rights, sensitivity, evidence, policy, scale, time, and source-role validation.
- **Candidate-as-authority:** treating schema validation as approval or execution.
- **Synthetic-as-production:** using the rehearsal helper against a real release root or representing its report as release evidence.
- **Invented CLI:** documenting or running a command that current repository evidence does not establish.
- **History deletion:** deleting the affected release, receipt, proof, source capture, review, or notice to hide a defect.
- **Data-plane authority collapse:** storing the release decision in `data/rollback/geology/`.
- **Carrier-as-truth:** treating tiles, catalogs, reports, graph edges, cross-sections, 3D scenes, screenshots, or AI answers as sovereign evidence.
- **Role collapse:** restoring permit, production, estimate, reserve, occurrence, deposit, model, observation, or interpretation as interchangeable.
- **Precision leak:** placing exact restricted geometry, proprietary detail, or reverse-engineering parameters in public candidates, notices, logs, or invalidation records.
- **Cross-lane overwrite:** using Geology recovery to rewrite Hydrology, Hazards, Soil, People/Land, Archaeology, or Infrastructure authority.
- **Partial invalidation:** leaving search, vector, AI, tile, CDN, catalog, triplet, report, or deep-link surfaces on the affected release.
- **Self-review at material consequence:** author, approver, executor, and verifier collapse without a documented bootstrap exception and appropriate controls.
- **Documentation-as-publication:** treating a merged runbook or green workflow as release, deployment, or publication.

[Back to top](#top)

---

## 17. Related surfaces

### Governing placement and lane documentation

- [`docs/runbooks/README.md`](../README.md)
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)
- [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [`docs/domains/geology/README.md`](../../domains/geology/README.md)
- [`docs/domains/geology/DATA_LIFECYCLE.md`](../../domains/geology/DATA_LIFECYCLE.md)
- [`docs/domains/geology/SENSITIVITY.md`](../../domains/geology/SENSITIVITY.md)

### Shared rollback contract and validation

- [`contracts/release/rollback_card.md`](../../../contracts/release/rollback_card.md)
- [`schemas/contracts/v1/release/rollback_card.schema.json`](../../../schemas/contracts/v1/release/rollback_card.schema.json)
- [`tools/validators/release/validate_rollback_card.py`](../../../tools/validators/release/validate_rollback_card.py)
- [`tests/validators/test_validate_rollback_card.py`](../../../tests/validators/test_validate_rollback_card.py)

### Rehearsal

- [`docs/runbooks/rollback-rehearsal.md`](../rollback-rehearsal.md)
- [`tools/release/rollback_apply.py`](../../../tools/release/rollback_apply.py)
- [`tests/release/test_synthetic_rollback_rehearsal.py`](../../../tests/release/test_synthetic_rollback_rehearsal.py)

### Geology release and data lanes

- [`release/candidates/geology/README.md`](../../../release/candidates/geology/README.md)
- [`release/rollback_cards/README.md`](../../../release/rollback_cards/README.md)
- [`release/correction_notices/README.md`](../../../release/correction_notices/README.md)
- [`release/manifests/README.md`](../../../release/manifests/README.md)
- [`data/rollback/geology/README.md`](../../../data/rollback/geology/README.md)
- [`data/published/geology/README.md`](../../../data/published/geology/README.md)
- [`tests/domains/geology/README.md`](../../../tests/domains/geology/README.md)
- [`policy/domains/geology/README.md`](../../../policy/domains/geology/README.md)

[Back to top](#top)

---

## 18. Evidence basis

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Current target at `main@a125b5b...` | CONFIRMED | Existing same-path runbook and prior blob identity | Prior prose did not prove current implementation |
| Accepted ADR-0029 + Directory Rules blob | CONFIRMED / accepted | Same-path placement under `docs/runbooks/geology/` and authority separation | Does not authorize release or rollback |
| RollbackCard contract/schema | CONFIRMED repository bytes; contract status remains draft/PROPOSED | Current candidate meaning, exact field surface, finite vocabularies, non-authority state | Does not prove reference resolution, review, execution, or release |
| RollbackCard validator/tests | CONFIRMED executable code and focused tests present | No-network candidate shape/local-consistency validation | Results were not executed by this documentation edit unless separately recorded |
| Synthetic helper/tests | CONFIRMED executable code and tests present | Marker-protected deterministic rehearsal design and negative controls | Synthetic only; not Geology-specific or production authority |
| `release/candidates/geology/` directory inventory | CONFIRMED at pinned revision | Only README is tracked in the canonical candidate lane | Does not prove absence of external, historical, restricted, generated, or differently located material |
| Geology data rollback README | CONFIRMED draft documentation | Data-plane support boundary and Geology sensitivity/anti-collapse concerns | No rollback instance or release authority |
| Geology domain and sensitivity docs | CONFIRMED documentation | Domain scope, harmful-precision posture, source-role and claim-class risks | Machine policy enforcement and operational stewardship remain incomplete or unverified |
| Connected Drive geology architecture report | CONFIRMED source lineage | Rollback is not deletion or silent replacement; target proof/catalog verification, correction, receipt, review, and rollback records matter | PDF was written without mounted repo evidence; every implementation path in it was proposed and is subordinate to current repository evidence |
| Deployment/runtime/logs | UNKNOWN in this update | — | No production recovery, alias, cache, signer, deployment, or publication claim is made |

### Source reconciliation note

The connected Drive report proposed rollback patterns before a repository checkout was available. Its durable ideas are retained here—rollback is not deletion, a prior target must be verified, public claim changes require visible correction, and downstream carriers must be invalidated—but its speculative paths and object examples are not treated as current implementation. Current repository contracts, schemas, validators, tests, and adopted placement governance control this revision.

### Open verification

- Assign accountable Geology, release, rollback, correction, evidence, rights/sensitivity, source-role, and independent-review stewards.
- Establish whether and how production release aliases are resolved and locked.
- Establish admitted production invalidation mechanisms and receipts for all finite classes.
- Establish signer identity, key custody, deployment boundary, and recovery audit destination.
- Implement and review a Geology-specific synthetic rollback drill.
- Reconcile draft release-lane naming and authority overlaps without creating parallel RollbackCard homes.
- Verify hosted exact-head checks for any PR that changes this runbook.
- Keep publication, deployment, promotion, and live-source activation outside documentation-only changes.

[Back to top](#top)
