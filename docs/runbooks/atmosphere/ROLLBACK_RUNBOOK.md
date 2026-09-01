<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-atmosphere-rollback
title: Atmosphere Rollback Runbook
type: standard
profile: candidate-preparation-and-synthetic-rehearsal
version: v1.0
prior_version: v0.1
status: draft; repository-grounded; fixture-first; operational-rollback-hold; non-authoritative; non-publisher; not-for-life-safety
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Atmosphere, evidence, source-rights, sensitivity, Hazards-seam, correction, rollback, review, release, operations, and independent-review assignments remain NEEDS VERIFICATION; CODEOWNERS routing does not establish those authorities."
created: 2026-05-13
updated: 2026-08-24
policy_label: public; atmosphere; rollback; fixture-first; no-network; operational-hold; non-release; not-for-life-safety
current_path: docs/runbooks/atmosphere/ROLLBACK_RUNBOOK.md
owning_root: docs/
responsibility: "Explain how to classify an Atmosphere release defect, prepare a non-executing RollbackCard candidate, exercise the bounded synthetic rollback or withdrawal rehearsal, and hand unresolved operational action to governed authorities without mutating public state."
truth_posture: >-
  CONFIRMED same-path repository placement, accepted Directory Rules basis,
  current generic RollbackCard contract/schema/validator/fixtures, marker-protected
  synthetic rehearsal helper and tests, read-only rollback-drill workflow, one
  verified CODEOWNERS route, Atmosphere domain boundaries, and current operational
  holds / PROPOSED future actor assignments, accepted policy, operational rollback,
  alias mutation, external invalidation, public correction, and release authority /
  CONFLICTED generic release profile versus permissive Atmosphere-domain schema
  stub, rollback-card lane guidance versus accepted placement law, and legacy
  data/rollback guidance versus the accepted receipt target / UNKNOWN production
  aliases, deployed public surfaces, external caches, signer custody, operational
  source-rights state, and operator capacity; cite-or-abstain
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 991f9f99634ceeb31228b22e593b1111f9b0510b
  target_prior_blob: fc9115d8506774adef82982770998d6576681946
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_decision: ADR-0029 accepted
  release_root_readme_blob: 60b6a656f8f2b765616bba7223f51c25863c7172
  rollback_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  release_rollback_schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  atmosphere_rollback_schema_blob: 10f2d0ddb9abd928a6e7679855706159c5c6ff48
  release_rollback_validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  generic_rollback_validator_stub_blob: b80dd40e93733c7fa76f8f9a78e9ec55b6090b4b
  rollback_pipeline_placeholder_blob: 2afd3a3d859318e05dcb3e1b2763e4e375b790b6
  synthetic_rehearsal_helper_blob: a8f6bff350e79b453f425ebce9a9ded6801f8944
  synthetic_rehearsal_test_blob: b644ca6c4185b3f81bc339c077eae85299833261
  rollback_drill_workflow_blob: 6ce891a99b3c192da17eb8ef25757b023b686f47
  atmosphere_placeholder_card_blob: ba00c2191e8b190059e729d6c70bf8c69d4fc2da
  atmosphere_stale_state_runbook_blob: 2b2050da0ef0e149101dc90478a0fb9c42417b63
  published_alias_adr_blob: db22ecff079e6522db45a3bb7c41c52ade029efb
  separation_of_duties_blob: 00f68beeeec7d57cce806e6cdbd710a837bd4f0c
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
inspection_boundary: >-
  Current-session GitHub reads of the target, accepted Directory Rules evidence,
  Atmosphere domain and sibling validation, correction, and stale-state runbooks,
  release-root guidance, RollbackCard
  contract and both schema lanes, validator and fixtures, rollback pipeline
  placeholder, synthetic rehearsal helper/tests, rollback-drill workflow,
  CODEOWNERS, separation-of-duties guidance, proposed published-alias ADR, and
  Atmosphere rollback support surfaces. Repository-native commands were not run
  in a mounted checkout while authoring. No live source was contacted, no actor
  was authenticated, no RollbackCard instance was issued, and no policy, review,
  correction, withdrawal, rollback, release, deployment, promotion, publication,
  alert, health determination, or regulatory action was performed.
related:
  - docs/runbooks/README.md
  - docs/runbooks/ROLLBACK_RUNBOOK.md
  - docs/runbooks/atmosphere/README.md
  - docs/runbooks/atmosphere/VALIDATION_RUNBOOK.md
  - docs/runbooks/atmosphere/STALE_STATE_RUNBOOK.md
  - docs/runbooks/atmosphere/CORRECTION_RUNBOOK.md
  - docs/runbooks/atmosphere/PROMOTION_RUNBOOK.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md
  - docs/governance/SEPARATION_OF_DUTIES.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/OBSERVED_MODELED_SEPARATION.md
  - docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - docs/domains/atmosphere/SENSITIVITY.md
  - release/README.md
  - release/rollback_cards/README.md
  - release/rollback_cards/rel-atmosphere-pm25-2026-001.card.json
  - contracts/release/rollback_card.md
  - schemas/contracts/v1/release/rollback_card.schema.json
  - schemas/contracts/v1/domains/atmosphere/rollback_card.schema.json
  - fixtures/release/rollback_card/
  - tools/validators/release/validate_rollback_card.py
  - tools/validators/validate_rollback_card.py
  - tools/release/rollback_apply.py
  - pipelines/rollback/main.py
  - tests/validators/test_validate_rollback_card.py
  - tests/release/test_synthetic_rollback_rehearsal.py
  - .github/workflows/rollback-card.yml
  - .github/workflows/rollback-drill.yml
  - .github/CODEOWNERS
  - data/rollback/atmosphere/README.md
tags: [kfm, runbook, atmosphere, air, rollback, withdrawal, correction, rollback-card, synthetic-rehearsal, source-role, evidence, rights, sensitivity, hazards-seam, governance, operational-hold]
notes:
  - "Same-path modernization under accepted ADR-0029; no root, lane, contract, schema, policy, fixture, validator, test, workflow, receipt, proof, release object, alias, or public state is created or moved."
  - "The generic release RollbackCard 1.0.0 profile is the current bounded validator target. The Atmosphere-domain rollback-card schema remains a permissive greenfield stub and is not an equivalent authority surface."
  - "Operational rollback remains HOLD: the production pipeline is a placeholder, the generic validator entrypoint delegates only to the bounded canonical validator, the published-alias decision remains proposed, and the available apply helper is synthetic-workspace-only."
  - "This runbook is an instruction and review-handoff surface. It is not a RollbackCard, ReviewRecord, PolicyDecision, CorrectionNotice, release approval, rollback receipt, or execution record."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Rollback Runbook

> **Repository-grounded procedure for classifying an Atmosphere / Air release defect, preparing a non-executing `RollbackCard` candidate, exercising the deterministic synthetic rollback or withdrawal rehearsal, and handing unresolved operational action to the appropriate governed authorities.**

<p>
  <img alt="Document status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-1f8fff">
  <img alt="Profile: fixture first" src="https://img.shields.io/badge/profile-fixture%20first-8250df">
  <img alt="Network: denied" src="https://img.shields.io/badge/network-denied-b42318">
  <img alt="Operational rollback: hold" src="https://img.shields.io/badge/operational%20rollback-HOLD-b42318">
  <img alt="Publication effect: none" src="https://img.shields.io/badge/publication-none-6e7781">
</p>

> [!IMPORTANT]
> **This runbook does not authorize or execute rollback.** The current repository proves a closed, fixture-first `RollbackCard` candidate profile and a marker-protected synthetic-workspace rehearsal. It does not prove authenticated rollback authority, accepted live policy, independent review, production alias mutation, external cache invalidation, release, deployment, promotion, or publication.

> [!WARNING]
> **KFM is not an official AQI, medical, regulatory, emergency-alerting, or life-safety authority.** Do not use this runbook to declare current air quality, certify a concentration, issue health guidance, originate an alert, or replace an agency advisory. Atmosphere may carry observation and advisory context; the Hazards lane and official issuers retain their own authority.

> [!CAUTION]
> [`tools/release/rollback_apply.py`](../../../tools/release/rollback_apply.py) is guarded for synthetic roots only. Do not weaken, bypass, rename around, or copy around its `.kfm-synthetic-rollback-rehearsal` marker and `synthetic: true` checks. Do not point it at the repository's real `data/`, `release/`, cache, storage, deployment, or public-delivery paths.

**Quick navigation:** [Purpose](#1-purpose-scope-and-non-goals) · [Authority](#2-authority-and-current-repository-evidence) · [Invariants](#3-atmosphere-fail-closed-invariants) · [Triggers](#4-trigger-classification-and-finite-candidate-dispositions) · [Preconditions](#5-preconditions-and-stop-conditions) · [Procedure](#6-candidate-preparation-and-synthetic-rehearsal-procedure) · [Contract](#7-current-rollbackcard-profile-and-schema-conflict) · [Rehearsal](#8-synthetic-rehearsal-and-safe-entry-points) · [Domain risks](#9-atmosphere-specific-defects-rights-sensitivity-and-hazards-seam) · [Disposition](#10-correction-stale-state-withdrawal-rollback-and-erasure) · [Invalidation](#11-carrier-and-derivative-invalidation-plan) · [Validation](#12-validation-and-claim-boundaries) · [Handoff](#13-review-handoff-packet) · [Anti-patterns](#14-anti-patterns) · [Open work](#15-current-holds-and-open-verification) · [Related](#16-related-authorities-and-operational-surfaces) · [Maintenance](#17-maintenance-correction-and-document-rollback) · [Template](#appendix-a-non-executing-atmosphere-candidate-template) · [Commands](#appendix-b-command-and-path-matrix)

---

## 1. Purpose, scope, and non-goals

### Purpose

Use this runbook after an Atmosphere artifact, claim, or public-facing carrier is suspected of being wrong, unsupported, impermissible, unsafe, or release-inconsistent. The operator's bounded responsibilities are to:

1. freeze the exact subject and repository revision;
2. classify the defect without inventing an operational state;
3. preserve Atmosphere source-role and knowledge-character distinctions;
4. prepare a schema-paired, non-executing `RollbackCard` candidate;
5. validate candidate shape and local consistency with the current no-network profile;
6. run the synthetic rehearsal only in a marked disposable workspace;
7. enumerate correction, withdrawal, invalidation, review, and target dependencies;
8. produce a truthful review handoff that leaves operational action on `HOLD` when authority or implementation is absent.

### In scope

- Atmosphere / Air / Weather / Climate public-safe release carriers and claims, including station and observation views, PM2.5 and ozone products, smoke and aerosol context, weather and climate layers, catalog projections, governed API payloads, Evidence Drawer content, Focus Mode answers, exports, and downstream indexes.
- Candidate rollback, withdrawal, hold, and error planning using the generic release `RollbackCard` 1.0.0 profile.
- Deterministic, no-network candidate validation and synthetic rehearsal in isolated temporary roots.
- Atmosphere-specific source-role, knowledge-character, unit, time, freshness, rights, sensitivity, and Hazards-boundary checks.
- Public-safe incident and review handoff material.
- Correction, withdrawal, invalidation, lineage, and rollback-target planning.

### Out of scope

- **Production rollback execution.** [`pipelines/rollback/main.py`](../../../pipelines/rollback/main.py) remains a one-line greenfield placeholder.
- **Live alias mutation.** The logical published-alias decision in [ADR-0015](../../adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md) remains proposed, and no production alias/operator is established by this runbook.
- **Release approval or public mutation.** A runbook, candidate card, passing validator, green workflow, commit, pull request, or merge cannot approve or perform a release transition.
- **Live source access.** Do not contact EPA, KDHE, NOAA/NWS, Kansas Mesonet, community-sensor, satellite, model, or other upstream services through this procedure.
- **Database, schema, graph, or policy-bundle rollback.** Those changes require their owning migration and rollback procedures.
- **UI-only code rollback.** Renderer or feature-flag changes that do not alter governed release meaning belong to the relevant UI/runtime procedure.
- **Erasure.** Rollback, withdrawal, correction, and tombstoning do not satisfy lawful deletion, privacy erasure, or rights-based removal by themselves.
- **Emergency action.** Atmosphere does not originate warnings, evacuation instructions, medical guidance, or exposure advice.

### State separation

| State or artifact | What it proves | What it does **not** prove |
|---|---|---|
| Tracked runbook | Human procedure exists at a reviewed commit | Operator authority or runtime readiness |
| Schema-valid `RollbackCard` candidate | Closed shape and bounded local consistency | Reference resolution, reviewer eligibility, policy approval, safe target, or execution |
| Candidate disposition | Proposed recovery posture | A public state transition |
| Synthetic rehearsal `PASS` | Deterministic behavior inside a marked temporary root | Production alias mutation, external invalidation, release, or publication |
| Hosted workflow success | Exact workflow assertions passed at one revision | Human approval, operational rollback, deployment, or public parity |
| Pull-request merge | Repository bytes entered `main` | `PUBLISHED` or rollback lifecycle state |
| Operational rollback | **UNKNOWN / HOLD** in current evidence | Must not be inferred from any state above |

[Back to top](#top)

---

## 2. Authority and current repository evidence

### 2.1 Directory Rules basis

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). This file is a human operational procedure at the existing path:

```text
docs/runbooks/atmosphere/ROLLBACK_RUNBOOK.md
```

The update is a same-path `PLACE` under the `docs/` responsibility root. It creates no new root, lane, contract, schema, policy, fixture, validator, test, workflow, receipt, proof, release record, alias, runtime, or public authority.

| Responsibility | Owning surface | Relationship to this runbook |
|---|---|---|
| Human Atmosphere rollback guidance | `docs/runbooks/atmosphere/` | **Owned here** |
| Atmosphere meaning and denials | [`docs/domains/atmosphere/`](../../domains/atmosphere/README.md) and its semantic authorities | Referenced; not redefined |
| Generic rollback meaning | [`contracts/release/rollback_card.md`](../../../contracts/release/rollback_card.md) | Current bounded semantic target |
| Generic candidate machine shape | [`schemas/contracts/v1/release/rollback_card.schema.json`](../../../schemas/contracts/v1/release/rollback_card.schema.json) | Current closed fixture-first profile |
| Atmosphere-domain schema stub | [`schemas/contracts/v1/domains/atmosphere/rollback_card.schema.json`](../../../schemas/contracts/v1/domains/atmosphere/rollback_card.schema.json) | Disclosed as incomplete/conflicted; not selected as equivalent authority |
| Candidate validation | [`tools/validators/release/validate_rollback_card.py`](../../../tools/validators/release/validate_rollback_card.py) | Bounded no-network validation only |
| Synthetic rehearsal | [`tools/release/rollback_apply.py`](../../../tools/release/rollback_apply.py) and release tests | Temporary marked roots only |
| Release decisions and targets | [`release/`](../../../release/README.md) | Separate append-only decision plane |
| Executed rollback/invalidation receipts | `data/receipts/rollback/` under accepted placement law | Separate execution-memory family; current operational producer unproved |
| Public-safe carriers | `data/published/` through governed delivery | Not read or mutated by this runbook |
| Reviewer routing | [`.github/CODEOWNERS`](../../../.github/CODEOWNERS) | GitHub routing only; not actor authority or independent review |
| Policy, rights, sensitivity, review, and release approval | Accepted policy and accountable state-bearing records | **UNKNOWN / HOLD** for operational use |

### 2.2 Current bounded status at the evidence snapshot

| Surface | Current repository evidence | Safe conclusion |
|---|---|---|
| Target path | Existing v0.1 proposed scaffold, blob `fc9115d8…` | Same-path replacement is supported and needed |
| Directory governance | ADR-0029 accepted; Directory Rules bytes pinned | Human runbook placement is confirmed |
| Generic `RollbackCard` contract | Draft v1.0 semantics paired to a closed 1.0.0 schema | Candidate meaning and bounded invariants are inspectable |
| Generic release schema | Draft 2020-12 JSON Schema, `additionalProperties: false` | Candidate shape is closed; governance effects must remain false |
| Release validator | Implemented, no-network, file-size bounded, duplicate-key aware, schema + semantic checks | Candidate shape and local consistency can be tested |
| Release fixtures | Three valid candidates and six invalid candidates with expected findings | Fixture polarity is testable |
| Atmosphere-domain rollback schema | Permissive id-only greenfield stub; `additionalProperties: true` | **CONFLICTED / HOLD**; do not treat as equivalent to the generic release profile |
| Atmosphere domain contract / fixtures / validator | Declared by the stub but absent at the snapshot | Domain-specific rollback validation is not established |
| Generic validator entry point | `tools/validators/validate_rollback_card.py` delegates to the canonical release validator | Bounded compatibility validation only; no execution authority |
| Production rollback pipeline | `pipelines/rollback/main.py` is a one-line placeholder | No production rollback engine is established |
| Synthetic helper | Marker-protected, no-network, deterministic; PLAN by default; APPLY only inside a marked synthetic root | Safe for rehearsal only |
| Synthetic tests | Eight non-vacuous tests cover plan/no-write, rollback, withdrawal, marker, synthetic flag, invalidations, target, and digest failures | Rehearsal behavior has bounded deterministic proof |
| `rollback-drill` workflow | Read-only; no release/signing secret; asserts holds and fixture behavior | Readiness inspection, not operational rollback |
| Atmosphere root card JSON | Proposed documentation placeholder with no schema `id` | Not a schema-admissible candidate, approval, or execution record |
| ADR-0015 alias decision | Draft / effective proposed | No accepted live alias model or operator |
| CODEOWNERS | One verified route, `@bartytime4life` | Review routing exists; independence and release authority do not |
| Separation of duties | ADR-0024 proposed; operational actor/assignment/review authority remains held | Operational SoD is `UNKNOWN / HOLD` |
| External runtime | No deployed alias, cache, public endpoint, or rollback dashboard was established by this inspection | Production behavior remains `UNKNOWN` |

### 2.3 Evidence hierarchy for a rollback case

Use this order when a case packet contains conflicting claims:

1. accepted trust, lifecycle, public-boundary, correction, and rollback invariants;
2. accepted ADRs and adopted Directory Rules;
3. current contracts, schemas, policy, code, tests, workflows, and immutable release evidence;
4. state-bearing evidence, review, correction, and release records;
5. this runbook and other explanatory documentation;
6. screenshots, badges, model language, issue summaries, and memory.

A commit proves bytes exist at a commit. It does not prove that a source was admitted, a target is safe, a policy was evaluated, a reviewer was eligible, or a public state changed.

[Back to top](#top)

---

## 3. Atmosphere fail-closed invariants

These invariants apply to every candidate and rehearsal.

1. **Candidate is not action.** A `RollbackCard` candidate cannot claim authority, completed policy, completed review, executed rollback, public mutation, or release.
2. **Evidence must remain separate and resolvable.** `evidence_bundle_refs` name support; their presence does not prove resolution. Operational action remains `HOLD` until each required `EvidenceRef` resolves to an admissible `EvidenceBundle`.
3. **Source roles must not collapse.** Regulatory archives, public AQI reports, observed sensors, low-cost sensors, satellite aerosol products, model fields, forecasts, and advisory context retain distinct knowledge characters.
4. **AQI is not concentration.** Never relabel an index as a measured concentration.
5. **AOD is not PM2.5.** Aerosol optical depth is a remotely sensed column property, not a surface PM2.5 observation.
6. **Model and forecast fields are not observations.** A modeled smoke or weather field cannot be promoted into `AirObservation` or `PM25Observation` merely because it looks plausible.
7. **Low-cost sensor release requires caveats.** Correction method, calibration context, humidity transferability, confidence, uncertainty, and limitations remain visible.
8. **Atmosphere is not alert authority.** Advisory context preserves issuer, valid/effective time, stale state, and official-source redirect; it does not become KFM-authored life-safety instruction.
9. **Stale and wrong are different.** A source outage or freshness expiry may require a visible stale state. Rollback is considered when the released claim or carrier is wrong, unsupported, unsafe, or impermissible.
10. **Public clients stay behind the trust membrane.** No rollback procedure grants direct access to RAW, WORK, QUARANTINE, internal stores, source credentials, graph internals, vector indexes, or direct model runtimes.
11. **History is preserved.** Rollback is not deletion, silent overwrite, or tile-byte mutation. The affected release and its audit lineage remain inspectable unless a separate lawful restriction applies.
12. **Sensitive joins fail closed.** Exact station, facility, private sensor, archaeology, rare-species, infrastructure, or living-person joins must not escape through an Atmosphere carrier or incident packet.
13. **Corrections are first-class.** A public-facing substantive defect may require a separate `CorrectionNotice`; the RollbackCard does not replace it.
14. **No invented operational interface.** Use only verified repository commands and files. Do not invent a `kfm release rollback` CLI, route, DTO, alias path, or cache API.

[Back to top](#top)

---

## 4. Trigger classification and finite candidate dispositions

### 4.1 Trigger reason codes

The current generic schema defines the following finite trigger codes. Atmosphere-specific detail belongs in the public-safe case narrative and evidence references, not in an unregistered machine code.

| Current schema code | Atmosphere example | Initial posture |
|---|---|---|
| `RELEASE_DEFECT` | Published layer manifest points at the wrong immutable carrier | Evaluate rollback or withdrawal candidate |
| `EVIDENCE_CONTRADICTION` | Evidence no longer supports the PM2.5 or smoke claim | Withdraw affected claim; evaluate prior supported release |
| `RIGHTS_CHANGE` | Redistribution terms changed after release | Withdraw or hold; prior target must be rights-rechecked |
| `SENSITIVITY_DISCOVERY` | A precise station/facility/sensitive join escaped the intended tier | Contain and withdraw; evaluate generalized prior target |
| `VALIDATION_FAILURE` | AQI labeled as concentration, AOD labeled as PM2.5, model labeled as observed, unit/time/CRS defect | Evaluate correction plus rollback or withdrawal |
| `SOURCE_WITHDRAWAL` | Upstream archive or source snapshot is withdrawn | Withdraw unsupported claim; evaluate a supported prior target |
| `POLICY_FAILURE` | Released carrier lacks required rights, evidence, review, or caveat posture | Hold or withdraw; do not select a target until policy is supportable |
| `SECURITY_ISSUE` | Release exposes a credential-bearing URL, restricted endpoint, or harmful precision | Emergency containment and restricted escalation |
| `OPERATIONAL_FAILURE` | Carrier cannot be served safely or consistently, without changing the underlying truth claim | Evaluate withdrawal or operational recovery; do not imply scientific correction |
| `EMERGENCY_HOLD` | Public safety or active exploitation risk requires immediate containment | Hold/withdraw and escalate; do not publish sensitive detail |
| `INSUFFICIENT_EVIDENCE` | No safe prior target can be shown to have evidence closure | `HOLD`; do not guess a rollback target |
| `INPUT_INVALID` | Candidate, manifest, digest, or scenario is malformed | `ERROR`; correct the input before any further action |

### 4.2 Candidate dispositions

The current `RollbackCard` schema does **not** use `ANSWER`, `ABSTAIN`, or `DENY` as card dispositions. It uses exactly:

| Disposition | Meaning | Public-state effect |
|---|---|---|
| `ROLLBACK_CANDIDATE` | Proposes a distinct prior release for later governed evaluation | None |
| `WITHDRAWAL_CANDIDATE` | Proposes withdrawal without selecting a prior release | None |
| `HOLD` | Records that recovery cannot proceed safely yet | None |
| `ERROR` | Records an invalid or failed candidate evaluation | None |

All candidate governance flags remain false. A later operational system may have its own finite response envelope, but this runbook must not invent or conflate it with the candidate contract.

### 4.3 Stale versus wrong

| Condition | Example | Default handling |
|---|---|---|
| Stale but still correctly described | A station feed missed its freshness interval, and the UI clearly labels the last observed time | Mark stale, narrow claims, and refresh through source procedures; rollback is not automatic |
| Wrong or misleading | AQI rendered as concentration or AOD rendered as ground PM2.5 | Contain; open correction and rollback/withdrawal evaluation |
| Unsupported | Evidence bundle or source descriptor no longer resolves | Withdraw or hold until support is restored |
| Impermissible | Rights or sensitivity posture no longer permits exposure | Withdraw/hold; target must independently pass current rights and sensitivity review |
| Operationally unavailable | CDN or API outage with intact immutable release evidence | Use operations recovery; do not rewrite scientific meaning |

[Back to top](#top)

---

## 5. Preconditions and stop conditions

### 5.1 Candidate-preparation preconditions

Before creating a candidate file, record or verify:

- [ ] Exact repository revision and changed-area scope.
- [ ] Affected release reference; do not use a mutable display label as identity.
- [ ] Candidate disposition and matching target mode.
- [ ] Distinct prior release reference for `ROLLBACK_CANDIDATE`, or `null` target for withdrawal/hold.
- [ ] Public-safe trigger reason and timezone-aware detection time.
- [ ] Non-placeholder candidate `spec_hash` produced by the selected deterministic profile.
- [ ] Evidence, policy, and review references kept in separate arrays.
- [ ] Correction notice reference when `public_notice_required` is true.
- [ ] Canonically sorted, unique invalidation classes.
- [ ] Restoration target matches the prior-release target.
- [ ] Detection, decision, and effective times are ordered.
- [ ] Lineage is not self-referential.
- [ ] Every governance flag is false and `governance.release_ref` is `null`.
- [ ] No secret, credential, private endpoint, sensitive coordinate, health inference, or unredacted incident detail is present.

### 5.2 Operational stop conditions

Return or retain `HOLD` and escalate rather than implying execution when any of these is unresolved:

- no distinct prior release can be identified;
- the target manifest or artifact digests cannot be verified;
- evidence bundles, source descriptors, policy decisions, or required correction records do not resolve;
- target rights, sensitivity, source role, knowledge character, time support, or public-safe precision is unknown;
- independent reviewer eligibility or release authority is not established;
- the proposed alias mechanism, operator, invalidation adapters, external cache inventory, or execution receipts are absent;
- the issue involves active security exploitation, protected location detail, or life-safety content that cannot be handled in a public channel;
- proceeding would require weakening the synthetic marker, using the placeholder production pipeline, or treating a green check as authority.

Use `ERROR` for malformed input, schema failure, digest mismatch, unsafe path, missing synthetic marker, or other deterministic evaluation failure. Correct the error; do not silently reinterpret it as a successful hold or rollback.

[Back to top](#top)

---

## 6. Candidate preparation and synthetic rehearsal procedure

### Step 1 — Freeze the subject

In a local checkout, capture the exact revision and current working-tree state before preparing a case packet:

```bash
git rev-parse HEAD
git status --short
```

Record the affected release reference, affected Atmosphere scope, public-facing carriers, discovered time, reporter, and public-safe defect summary. Do not paste sensitive coordinates, credentials, private URLs, raw health information, or exploit details into a public issue or pull request.

### Step 2 — Classify and contain

Select one current trigger reason code and one candidate disposition. Separate these questions:

1. Is the material stale, wrong, unsupported, impermissible, or operationally unavailable?
2. Is a public correction notice required?
3. Is there a demonstrably distinct prior release candidate?
4. Which carriers and derivatives may depend on the affected release?
5. Which authority, evidence, policy, review, and execution dependencies remain unresolved?

Containment of a real public surface is an operational decision outside this documentation procedure. Record the need; do not claim that it occurred.

### Step 3 — Prepare the candidate against the generic profile

Start from the reviewed fixture rather than the Atmosphere-domain stub:

```text
fixtures/release/rollback_card/valid/valid_prior_release_candidate.json
```

Populate the current 1.0.0 field set described in [§7](#7-current-rollbackcard-profile-and-schema-conflict). Keep governance effects false. Do not turn the existing Atmosphere placeholder card into an operational record by adding plausible fields without an authorized case and review path.

### Step 4 — Validate candidate shape and local consistency

```bash
python tools/validators/release/validate_rollback_card.py \
  <candidate-card.json>
```

Expected output is deterministic JSON with `outcome` `PASS` or `FAIL`, findings, and scope `rollback-card-candidate-shape-and-local-consistency-only`.

A `PASS` does not resolve any referenced object, authenticate a reviewer, execute policy, prove target safety, or mutate public state.

### Step 5 — Run the current fixture and unit profiles

```bash
python tools/validators/release/validate_rollback_card.py --fixtures

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose

python -m unittest -q \
  tests.release.test_synthetic_rollback_rehearsal
```

`python tools/validators/validate_rollback_card.py` is the historical compatibility entry point and delegates to the canonical release validator. A PASS has the same bounded meaning as the canonical CLI and does not authorize rollback execution.

### Step 6 — Prepare a disposable synthetic workspace

Use only a temporary root built from synthetic release manifests and artifacts. The root must contain the exact marker:

```text
.kfm-synthetic-rollback-rehearsal
```

with exact content:

```text
synthetic-only
```

The scenario must declare `synthetic: true`. Never copy real release credentials, live endpoints, private data, or production storage mounts into the rehearsal root.

### Step 7 — Run PLAN mode first

```bash
python tools/release/rollback_apply.py \
  --workspace <marked-synthetic-workspace> \
  --scenario <synthetic-scenario.json> \
  --report <plan-report.json>
```

PLAN is the default and must not write correction, invalidation, or alias files. Run it twice and compare outputs when deterministic replay matters.

### Step 8 — Run APPLY only inside the disposable marked root

```bash
python tools/release/rollback_apply.py \
  --workspace <marked-synthetic-workspace> \
  --scenario <synthetic-scenario.json> \
  --report <apply-report.json> \
  --apply
```

Synthetic APPLY may change only the marked temporary workspace. It must preserve the affected synthetic release, write a synthetic correction record and complete invalidation record, and report that no authority, policy, review, release, publication, or real public mutation occurred.

### Step 9 — Capture a review handoff and stop

Attach or summarize:

- exact repository and candidate digests;
- validator and test commands with exit status;
- candidate findings and disposition;
- synthetic PLAN/APPLY report digests, when run;
- carrier and derivative inventory;
- evidence, policy, review, correction, target, rights, sensitivity, and Hazards-seam gaps;
- introduced, inherited, expected, pending, not-run, and unknown failures separately;
- explicit statement that operational rollback remains `HOLD`.

Do not mutate a real alias, publish a correction, clear a cache, deploy a service, or mark the candidate approved from this procedure.

[Back to top](#top)

---

## 7. Current RollbackCard profile and schema conflict

### 7.1 Generic release profile selected for bounded validation

The current generic schema requires every candidate to contain:

| Field | Required | Bounded role |
|---|---:|---|
| `object_type` | yes | Constant `RollbackCard` |
| `schema_version` | yes | Constant `1.0.0` |
| `id` | yes | Stable card identifier matching the schema pattern |
| `version` | yes | Candidate semantic version |
| `spec_hash` | yes | Non-zero SHA-256 binding for the selected candidate profile |
| `disposition` | yes | `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, or `ERROR` |
| `trigger` | yes | Registered reason code and timezone-aware detection time |
| `affected_release_ref` | yes | Release whose current use is under review |
| `target` | yes | Prior-release, withdrawal, or hold target |
| `evidence_bundle_refs` | yes | Sorted, unique evidence support references |
| `policy_decision_refs` | yes | Sorted, unique policy references |
| `review_record_refs` | yes | Sorted, unique review references; presence is not approval |
| `correction_notice_ref` | yes | Notice reference or `null` when no public notice is required |
| `invalidations` | yes | One or more registered carrier classes |
| `restoration` | yes | Intended target, public-notice need, and mandatory revalidation |
| `timing` | yes | Decision and optional effective time |
| `lineage` | yes | Prior/later card references without self-supersession |
| `governance` | yes | Explicit non-authority state |

The current schema and validator require a rollback candidate to name a distinct prior target and provide non-empty evidence and policy arrays. They do not verify that those references resolve or that the target is actually safe.

### 7.2 Governance boundary

Every fixture-first candidate must keep these values:

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

Any contrary value fails the profile with `GOVERNANCE_BOUNDARY_VIOLATION`.

### 7.3 Atmosphere-domain schema conflict

The parallel Atmosphere schema currently:

- requires only `id`;
- allows arbitrary additional properties;
- describes itself as a greenfield placeholder;
- names a domain contract, fixture root, and validator that were not present at the evidence snapshot.

Therefore:

- use the generic release profile for the current bounded candidate check;
- do not merge the schemas in prose;
- do not call the Atmosphere stub an extension or equivalent profile;
- do not create a new parallel schema home from this runbook;
- record any future domain-specific fields through an accepted contract/schema compatibility decision.

### 7.4 Other visible drift

- `release/rollback_cards/README.md` still describes compact review cards, while accepted Directory Rules and the current generic contract assign this lane rollback decision/candidate semantics. Treat the README as documentation drift, not stronger authority.
- `release/rollback_cards/rel-atmosphere-pm25-2026-001.card.json` is a four-field documentation placeholder. It has no schema `id` and is not a valid `RollbackCard` candidate.
- `data/rollback/atmosphere/README.md` contains useful domain guardrails but reflects older two-plane and path assumptions. Accepted placement now points executed rollback and invalidation receipts toward `data/receipts/rollback/`; migration remains separate work.
- ADR-0015 remains proposed. It does not authorize a live mutable alias.

[Back to top](#top)

---

## 8. Synthetic rehearsal and safe entry points

### 8.1 What the helper currently proves

| Behavior | Current bounded evidence |
|---|---|
| Root guard | Exact marker file required; symlink and marker-content checks fail closed |
| Scenario guard | `synthetic: true` required; only `ROLLBACK` or `WITHDRAWAL` accepted |
| Path safety | Absolute, parent-traversal, escaping, and unsafe-symlink paths are rejected |
| Digest checks | Current alias, affected manifest/artifacts, and target manifest/artifacts are verified inside the temporary root |
| PLAN mode | Deterministic report; no correction/invalidation/alias writes |
| APPLY mode | Synthetic alias transition or withdrawal, correction record, and full invalidation record inside the marked root |
| History | Affected synthetic manifest and artifacts remain byte-preserved |
| Failure posture | Deterministic `HOLD` report with reason code; no real public mutation |
| Governance | All authority/release/public effects remain false; `synthetic_workspace_only` is true |

### 8.2 Current test coverage

The tracked test profile includes non-vacuous cases for:

1. deterministic no-write PLAN;
2. rollback alias switch with history preservation and invalidation;
3. withdrawal while retaining the affected release;
4. denial of non-synthetic input;
5. denial of incomplete invalidation inventory;
6. denial of missing target release;
7. denial of artifact digest mismatch;
8. denial when the synthetic marker is absent.

### 8.3 Workflow boundary

`.github/workflows/rollback-drill.yml` is a read-only readiness workflow. It intentionally confirms that:

- the production rollback pipeline remains a placeholder;
- the generic compatibility validator delegates to the schema-declared canonical validator and must preserve fixture-output parity;
- the release candidate profile and fixtures pass their bounded validation;
- the synthetic helper retains its marker and no-authority guards;
- the rehearsal tests are non-vacuous;
- root card JSON files remain documentation placeholders;
- no production rollback, target mutation, invalidation, release, or publication is performed.

Do not rename the workflow or its established job IDs merely to avoid a failing check. Reconcile changed behavior deliberately if the implementation later graduates.

[Back to top](#top)

---

## 9. Atmosphere-specific defects, rights, sensitivity, and Hazards seam

### 9.1 Defect matrix

| Defect | Why it matters | Candidate and correction posture |
|---|---|---|
| AQI presented as concentration | AQI is an index derived from breakpoints, not a direct concentration measurement | `VALIDATION_FAILURE`; correction required; evaluate prior correctly labeled release or withdrawal |
| AOD presented as PM2.5 | AOD is a column optical property, not surface PM2.5 | `VALIDATION_FAILURE`; withdraw misleading claim; evaluate role-correct prior target |
| Model or forecast presented as observed | Model output cannot substitute for an observation | `VALIDATION_FAILURE` or `EVIDENCE_CONTRADICTION`; correction plus rollback/withdrawal evaluation |
| Low-cost sensor without caveats | Calibration, humidity response, transferability, uncertainty, and limitations affect interpretation | `POLICY_FAILURE` or `VALIDATION_FAILURE`; hold/withdraw until caveat-bearing target is supportable |
| Unit or averaging-period defect | µg/m³, ppb, AQI, hourly, daily, and rolling-window values are not interchangeable | `VALIDATION_FAILURE`; correct and evaluate prior valid release |
| Time-facet collapse | Observed, valid, issue, retrieval, publication, and correction times carry different meaning | `VALIDATION_FAILURE`; re-key and revalidate before any release decision |
| Geometry or CRS defect | Wrong location or footprint can misstate exposure and provenance | `RELEASE_DEFECT` or `VALIDATION_FAILURE`; contain, correct, and evaluate prior valid geometry |
| Stale/decommissioned station shown as live | Freshness and station state affect public interpretation | Mark stale when accurate; use withdrawal/rollback only if the released representation is misleading |
| Rights drift or source withdrawal | Previously public bytes may no longer be redistributable or supportable | `RIGHTS_CHANGE` or `SOURCE_WITHDRAWAL`; target requires independent current review |
| Sensitive station/facility or cross-domain join | Precise combinations can expose private operations, critical infrastructure, archaeology, rare species, or living persons | `SENSITIVITY_DISCOVERY`; restrict public detail and escalate through protected review |
| Hazards-boundary creep | Atmosphere context can be mistaken for official warning or life-safety instruction | `POLICY_FAILURE` or `EMERGENCY_HOLD`; contain KFM-authored surface and redirect to official issuer/Hazards |
| Uncited or role-collapsed Focus Mode answer | Generated language can amplify a release defect | Invalidate `AI_CACHE`; retry only through governed evidence; preserve prior AI receipt in audit lineage |
| Mutable tile or carrier bytes | In-place edits destroy release identity and correction lineage | `RELEASE_DEFECT` or `SECURITY_ISSUE`; preserve affected bytes and rebuild through governed release process |

### 9.2 Rights and source review

A prior release is not automatically safe merely because it was once published. Before an operational decision, current accountable reviewers must verify, for every material source:

- source identity and authority role;
- exact snapshot/version and content digest;
- redistribution, attribution, caching, and derivative terms;
- retention and withdrawal obligations;
- freshness and valid/effective time;
- sensitivity and location precision;
- model/observation/forecast/advisory character;
- whether the source itself has been corrected, withdrawn, or superseded.

Do not treat source-family names in this runbook as current admission or rights proof.

### 9.3 Sensitive and security incident handling

Public case records must use generalized, non-exploitable summaries. Route restricted details through an approved private incident channel when a case involves:

- credentials, tokens, signed URLs, or private endpoints;
- exact private-sensor, critical-infrastructure, facility-security, archaeology, or rare-species locations;
- living-person or health-related records;
- exploit steps or cache keys that would enable abuse;
- rights-holder or sovereign/community-restricted material.

The public handoff should contain a stable restricted-record reference, not the protected detail itself.

### 9.4 Hazards seam

Atmosphere may preserve issuer-authored warning/advisory context with source, issue time, valid/effective interval, and official redirect. It must not:

- originate an emergency instruction;
- convert a model field into warning truth;
- imply that rollback completion restores current safety;
- delay referral to the official issuing authority;
- expose a withdrawn official advisory as current.

When life-safety meaning is implicated, coordinate with the Hazards lane and official issuer while keeping the KFM release, evidence, correction, and rollback records distinct.

[Back to top](#top)

---

## 10. Correction, stale state, withdrawal, rollback, and erasure

Choose the narrowest posture that truthfully matches the defect.

| Posture | Use when | Required separation |
|---|---|---|
| Validation rejection | Candidate never crossed a governed release boundary | Use the validation runbook; no rollback card is needed merely to discard an unreleased candidate |
| Stale-state marker | Content remains correctly described but support is outside the freshness/review interval | Preserve last-observed and source times; narrow claims; do not silently refresh |
| Correction | Released meaning is wrong but a superseding corrected release can be prepared | Preserve prior release; issue/plan a `CorrectionNotice`; follow normal validation, policy, review, and release gates |
| Withdrawal candidate | Affected release must stop being current and no prior safe target is supportable | `WITHDRAWAL_CANDIDATE`; target release is `null`; preserve audit lineage |
| Rollback candidate | A distinct prior release is demonstrably available for later governed evaluation | `ROLLBACK_CANDIDATE`; target and restoration references must match |
| Hold | Evidence, rights, sensitivity, reviewer authority, target, or implementation is unresolved | `HOLD`; do not activate a plausible target |
| Error | Input or deterministic evaluation failed | `ERROR`; correct the failure before reevaluation |
| Erasure/restriction | Law, privacy, rights, security, sovereignty, or policy requires access removal beyond withdrawal | Use the governing removal/revocation process; rollback alone is insufficient |

A correction and rollback may be paired: correction explains the public meaning change; rollback identifies the proposed release transition. Neither substitutes for evidence, policy, review, release, execution, or receipts.

[Back to top](#top)

---

## 11. Carrier and derivative invalidation plan

The current schema allows exactly these invalidation classes:

```text
AI_CACHE
API_CACHE
CATALOG
CDN
DOWNSTREAM_DERIVATIVES
SEARCH_INDEX
TILES
TRIPLETS
VECTOR_INDEX
```

The array must be sorted and unique when populated. Select every class materially affected by the case; do not add invented values to the machine candidate.

| Class | Atmosphere impact to evaluate | Current operational status |
|---|---|---|
| `API_CACHE` | Feature detail, time-series, evidence, Focus request, and other governed response caches | Inventory and execution **UNKNOWN / HOLD** |
| `CDN` | Cached public-safe files or tile ranges | External endpoints and purge authority **UNKNOWN / HOLD** |
| `TILES` | PMTiles/MVT/raster/COG-derived layer references and browser caches | Synthetic invalidation only; no live adapter proved |
| `CATALOG` | STAC/DCAT/domain catalog records that identify the affected release | Operational propagation **UNKNOWN / HOLD** |
| `TRIPLETS` | Graph statements derived from the affected release | Operational graph invalidation **UNKNOWN / HOLD** |
| `SEARCH_INDEX` | Search documents and release-aware lookup entries | Operational index invalidation **UNKNOWN / HOLD** |
| `VECTOR_INDEX` | Retrieval embeddings derived from withdrawn material | Operational vector invalidation **UNKNOWN / HOLD** |
| `AI_CACHE` | Cached generated answers and candidate summaries tied to the release | Prior AI receipts remain audit records; runtime invalidation **UNKNOWN / HOLD** |
| `DOWNSTREAM_DERIVATIVES` | Exports, stories, dashboards, reports, screenshots, derived statistics, and other carriers | Must be enumerated case by case |

### Invalidation rules

1. Inventory dependencies before claiming closure.
2. Preserve immutable affected release bytes and state-bearing records.
3. Do not edit PMTiles, COG, GeoParquet, JSON, manifests, or generated answers in place to make the defect disappear.
4. A cache purge is not a correction or rollback decision.
5. A new map style, badge, screenshot, or AI answer is not proof that old derivatives were invalidated.
6. Record execution receipts separately from the RollbackCard candidate and from proof/evidence.
7. Read back every governed public surface before calling an operational case complete.

[Back to top](#top)

---

## 12. Validation and claim boundaries

### 12.1 What current checks prove

| Check | Proves | Does not prove |
|---|---|---|
| JSON Schema validation | Required shape, finite vocabularies, and closed properties | Source/evidence truth, actor authority, target safety, or execution |
| Release validator semantic checks | Local target/disposition, references, timing, correction, canonical-array, and governance consistency | Resolution of references, signatures, policy outcome, public mutation |
| Valid/invalid fixture profile | Expected polarity for the tracked examples | Coverage of every real Atmosphere failure |
| Synthetic rehearsal tests | Deterministic behavior and fail-closed guards in temporary marked roots | Production integration or external invalidation |
| `rollback-drill` hosted job | Exact readiness assertions at one commit | Rollback authority, alias mutation, release, deployment, or publication |
| Documentation/link checks | Runbook shape and navigation | Scientific correctness or operational readiness |

### 12.2 Exact-head reporting

For a pull request or case handoff, report each relevant check as one of:

- `PASS` — completed successfully at the exact head;
- `FAIL` — completed unsuccessfully at the exact head;
- `PENDING` — started or queued but not settled;
- `NOT_RUN` — applicable but not executed;
- `NOT_APPLICABLE` — not relevant to the changed area;
- `UNKNOWN` — evidence unavailable.

Separate failures introduced by the changed rollback surface from inherited repository failures. A docs-only pull request can still expose an inherited workflow failure; do not attribute it to the document without changed-area evidence.

### 12.3 Minimum candidate evidence

A candidate handoff should contain:

- candidate path and digest;
- selected schema and validator paths;
- validation output and exit code;
- expected/actual fixture polarity when fixtures changed;
- synthetic report path/digest when rehearsal ran;
- exact commit and workflow-run references;
- unresolved evidence, policy, rights, sensitivity, review, target, invalidation, and execution items;
- explicit non-effects: no authority, policy approval, review completion, rollback execution, public mutation, release, deployment, or publication.

[Back to top](#top)

---

## 13. Review handoff packet

Use a compact, public-safe packet with these sections.

### Identity

- Repository and exact commit.
- Affected release reference.
- Candidate card ID, version, and digest.
- Atmosphere scope, geography/time scope, and release-facing carrier families.

### Classification

- Stale, wrong, unsupported, impermissible, security-sensitive, or operationally unavailable.
- Current trigger reason code.
- Candidate disposition and target mode.
- Public notice requirement.

### Support

- EvidenceBundle references and resolution status.
- SourceDescriptor/snapshot references and source-role status.
- PolicyDecision references and whether an accepted evaluator actually ran.
- ReviewRecord references and reviewer eligibility/independence status.
- CorrectionNotice reference or reason it is not required.
- Rights, sensitivity, official-source, and Hazards-seam review status.

### Impact

- Complete invalidation-class list.
- Named carriers, caches, catalogs, triplets, search/vector indexes, AI caches, exports, stories, and dashboards affected.
- Public-safe containment need and current verified state.

### Validation

- Commands, exit codes, exact-head workflow runs, and candidate findings.
- Synthetic PLAN/APPLY report digests, when available.
- Introduced, inherited, expected, pending, not-run, and unknown failures.

### Decision boundary

State explicitly:

> Candidate preparation and synthetic rehearsal are complete only within their declared scope. No actor authority, live policy approval, independent review, rollback execution, alias mutation, external invalidation, release, deployment, promotion, or publication is established. Operational rollback remains `HOLD`.

[Back to top](#top)

---

## 14. Anti-patterns

Do not:

- use the Atmosphere id-only schema stub as though it were the current closed release profile;
- treat a compatibility-validator PASS as rollback approval, execution authority, or production readiness;
- invoke or replace the production pipeline placeholder with unreviewed logic;
- weaken the synthetic marker, `synthetic: true`, path, symlink, digest, or invalidation guards;
- point the synthetic helper at repository, release, cache, object-storage, database, or deployment paths;
- treat `release/rollback_cards/rel-atmosphere-pm25-2026-001.card.json` as a valid candidate or approval;
- invent `kfm release rollback` commands, public routes, alias files, DTOs, cache APIs, or owner identities;
- label AQI as concentration, AOD as PM2.5, model output as observation, or low-cost sensor output as regulatory evidence;
- use a source outage alone as proof that the released claim is wrong;
- roll back to a target whose current rights, sensitivity, evidence, or time support has not been checked;
- edit released carrier bytes or manifests in place;
- delete the affected release or prior AI receipt to hide the defect;
- publish sensitive coordinates, credentials, private endpoints, exploit details, or health inferences in a public case packet;
- treat CODEOWNERS routing, a second username, a bot, a green check, a review comment, or a merge as independent release authority;
- let an AI answer select a target, approve a rollback, or stand in for EvidenceBundle, policy, review, correction, or release evidence;
- describe a docs update, pull request, or merge as rollback, release, deployment, promotion, or publication.

[Back to top](#top)

---

## 15. Current holds and open verification

| Item | Current bounded status | Required before operational reliance |
|---|---|---|
| Production rollback pipeline | One-line placeholder | Accepted operator contract, implementation, negative tests, receipts, and review |
| Generic compatibility validator | **CONFIRMED delegation** | Preserve canonical/compatibility parity; validation remains non-executing |
| Generic release candidate profile | Closed, fixture-first, proposed | Accepted operational profile and reference-resolution layer |
| Atmosphere-domain schema | Permissive id-only stub | Contract/schema decision, closed shape, fixtures, validator, compatibility plan |
| Atmosphere domain contract/fixtures/validator | Absent at declared paths | Add only through a dependency-closed reviewed slice |
| Live published alias | Not established | Accepted ADR/profile, immutable releases, atomic CAS semantics, resolver, tests, receipts |
| ADR-0015 | Proposed | Human decision remains separate from implementation graduation |
| Rollback-card lane README | Vocabulary/authority drift | Reconcile in its own release-governance docs slice |
| Legacy `data/rollback/` lanes | Present with older guidance; accepted receipt target differs | Classified migration and compatibility/retention plan |
| Operational policy | No accepted complete release/rollback policy execution proved | Accepted source, evaluator, tests, version binding, and state-bearing decision |
| Reviewer independence | One CODEOWNERS route; ADR-0024 proposed | Authenticated actors, scoped assignments, conflicts/recusals, independent capacity |
| Source rights and terms | Provider-specific current state not checked here | Exact source/version/terms review for affected and target releases |
| Sensitive-precision handling | Doctrine documented; case-specific result absent | Approved transform, restricted review, and public-safe read-back |
| External invalidation | CDN/cache/search/vector/graph/AI adapters unproved | Inventory, least-privilege operators, deterministic receipts, negative tests |
| Public runtime parity | Unknown | Exact release, deployment, route, cache, and read-back evidence |
| Rollback drill cadence/SLO | No accepted operational cadence established | Steward decision, measurable acceptance criteria, operational evidence |
| Atmosphere operations ownership | Unassigned | Accepted stewardship and escalation paths |

The smallest credible follow-up is not a production rollback. It is a separately authorized, no-network slice that reconciles the Atmosphere schema stub with the generic candidate profile or adds one Atmosphere-specific negative fixture only after the contract and schema authority boundary is decided.

[Back to top](#top)

---

## 16. Related authorities and operational surfaces

### Governing placement and boundaries

- [Directory Rules v2](../../doctrine/directory-rules.md)
- [ADR-0029 — adopted Directory Rules](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [ADR-0015 — proposed published-alias decision](../../adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md)
- [Separation of Duties](../../governance/SEPARATION_OF_DUTIES.md)
- [Atmosphere domain README](../../domains/atmosphere/README.md)

### Sibling procedures

- [Atmosphere Validation Runbook](VALIDATION_RUNBOOK.md)
- [Atmosphere Stale-State Runbook](STALE_STATE_RUNBOOK.md)
- [Atmosphere Correction Runbook](CORRECTION_RUNBOOK.md)
- [Atmosphere Promotion Runbook](PROMOTION_RUNBOOK.md)
- [Parent KFM Rollback Runbook](../ROLLBACK_RUNBOOK.md) — useful lineage; verify current implementation claims independently

### Contracts and schemas

- [RollbackCard semantic contract](../../../contracts/release/rollback_card.md)
- [Generic release RollbackCard schema](../../../schemas/contracts/v1/release/rollback_card.schema.json)
- [Atmosphere rollback-card schema stub](../../../schemas/contracts/v1/domains/atmosphere/rollback_card.schema.json)

### Validation and rehearsal

- [Release RollbackCard validator](../../../tools/validators/release/validate_rollback_card.py)
- [Synthetic rollback helper](../../../tools/release/rollback_apply.py)
- [RollbackCard validator tests](../../../tests/validators/test_validate_rollback_card.py)
- [Synthetic rehearsal tests](../../../tests/release/test_synthetic_rollback_rehearsal.py)
- [RollbackCard fixtures](../../../fixtures/release/rollback_card/README.md)
- [`rollback-card` workflow](../../../.github/workflows/rollback-card.yml)
- [`rollback-drill` workflow](../../../.github/workflows/rollback-drill.yml)

### Release and support lanes

- [Release root](../../../release/README.md)
- [Rollback-card lane](../../../release/rollback_cards/README.md)
- [Atmosphere rollback support lane](../../../data/rollback/atmosphere/README.md) — current path presence; older placement assumptions require care

[Back to top](#top)

---

## 17. Maintenance, correction, and document rollback

### Update triggers

Review this runbook when any of these changes:

- generic RollbackCard contract, schema, validator, fixtures, or reason-code vocabulary;
- Atmosphere-domain rollback schema, contract, fixtures, or validator;
- synthetic helper guards, scenario shape, report shape, or tests;
- `rollback-card` or `rollback-drill` workflows;
- accepted published-alias decision or implementation;
- release, correction, withdrawal, review, policy, rights, sensitivity, or receipt placement;
- Atmosphere knowledge-character, source-role, Hazards-seam, or public-safety boundary;
- operational actor assignments, required checks, deployment, caches, or public routes.

### Correcting this runbook

A documentation defect is corrected through a normal reviewed docs change. Preserve the document ID and explain any changed operational meaning. Do not use a prose correction to amend a contract, schema, policy, workflow, or release state owned elsewhere.

### Rolling back this document change

Before merge, close the draft pull request or revert the branch commit. After merge, use a normal repository revert or corrective pull request against the exact merged commit. Reverting this Markdown restores documentation bytes only; it does not reverse any independent contract, schema, policy, release, deployment, or public state.

### Definition of done for this document

- Same-path placement remains supported by accepted Directory Rules.
- Current candidate, schema, validator, rehearsal, workflow, and operational-hold claims are repository-grounded.
- Atmosphere source-role and life-safety boundaries are visible.
- No invented command, route, owner, alias, policy result, or execution claim remains.
- Candidate validation, synthetic rehearsal, operational rollback, release, deployment, and publication are kept distinct.
- Links and anchors are valid at the reviewed revision.

[Back to top](#top)

---

<a id="appendix-a-non-executing-atmosphere-candidate-template"></a>

## Appendix A — Non-executing Atmosphere candidate template

> [!IMPORTANT]
> This template shows the current field families but is intentionally not a ready-to-submit JSON object. Replace every angle-bracket value from governed case evidence, compute the selected deterministic digest, keep arrays sorted and unique, and validate the result. Do not copy a plausible identifier or digest into a real case merely to obtain `PASS`.

```yaml
object_type: RollbackCard
schema_version: 1.0.0
id: rollback:atmosphere:<stable-case-id>
version: 1.0.0
spec_hash: sha256:<computed-64-lowercase-hex>
disposition: ROLLBACK_CANDIDATE
trigger:
  reason_code: VALIDATION_FAILURE
  detected_at: <timezone-aware-date-time>
affected_release_ref: <immutable-affected-release-ref>
target:
  mode: PRIOR_RELEASE
  release_ref: <distinct-prior-release-ref>
evidence_bundle_refs:
  - <resolved-or-pending-evidence-bundle-ref>
policy_decision_refs:
  - <policy-decision-ref>
review_record_refs: []
correction_notice_ref: <correction-notice-ref-or-null>
invalidations:
  - AI_CACHE
  - API_CACHE
  - CATALOG
  - CDN
  - DOWNSTREAM_DERIVATIVES
  - SEARCH_INDEX
  - TILES
  - TRIPLETS
  - VECTOR_INDEX
restoration:
  restore_release_ref: <same-distinct-prior-release-ref>
  public_notice_required: true
  validation_required: true
timing:
  decided_at: <timezone-aware-date-time>
  effective_at: null
lineage:
  supersedes: null
  superseded_by: null
governance:
  authority_created: false
  policy_evaluated: false
  review_completed: false
  rollback_executed: false
  public_state_mutated: false
  release_ref: null
```

Use the tracked valid fixture for an executable example:

```text
fixtures/release/rollback_card/valid/valid_prior_release_candidate.json
```

The fixture is synthetic and remains non-authoritative.

[Back to top](#top)

---

<a id="appendix-b-command-and-path-matrix"></a>

## Appendix B — Command and path matrix

| Purpose | Current path or command | Status / limit |
|---|---|---|
| Validate one candidate | `python tools/validators/release/validate_rollback_card.py <file>` | Implemented; candidate shape/local consistency only |
| Validate fixture profile | `python tools/validators/release/validate_rollback_card.py --fixtures` | Implemented, no-network |
| Run validator tests | `python -m unittest discover --start-directory tests/validators --pattern 'test_validate_rollback_card.py' --verbose` | Implemented focused tests |
| Run rehearsal tests | `python -m unittest -q tests.release.test_synthetic_rollback_rehearsal` | Implemented; temporary roots only |
| Plan synthetic scenario | `python tools/release/rollback_apply.py --workspace <root> --scenario <file> --report <file>` | Marker-protected synthetic root only |
| Apply synthetic scenario | Same command plus `--apply` | Disposable marked root only; no real public state |
| Compatibility validator | `python tools/validators/validate_rollback_card.py --fixtures` | Implemented delegate to the canonical validator; validation only, no rollback authority |
| Production pipeline | `pipelines/rollback/main.py` | **Do not use** — placeholder |
| Candidate semantic contract | `contracts/release/rollback_card.md` | Draft, proposed, schema-paired |
| Candidate schema | `schemas/contracts/v1/release/rollback_card.schema.json` | Closed fixture-first 1.0.0 profile |
| Atmosphere schema | `schemas/contracts/v1/domains/atmosphere/rollback_card.schema.json` | Permissive placeholder; conflicted |
| Root Atmosphere card | `release/rollback_cards/rel-atmosphere-pm25-2026-001.card.json` | Documentation placeholder; not schema-admissible |
| Hosted readiness | `.github/workflows/rollback-drill.yml` | Read-only inspection; operational hold |

[Back to top](#top)

---

<sub><sup>**Updated:** 2026-08-24 · **Document:** `kfm://doc/runbook-atmosphere-rollback` · **Status:** repository-grounded draft · **Operational rollback:** HOLD · **Release/deployment/publication effect:** none.</sup></sub>
