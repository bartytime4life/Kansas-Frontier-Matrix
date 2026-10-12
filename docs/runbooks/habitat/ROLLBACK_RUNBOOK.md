<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/habitat/rollback
title: Habitat — Rollback, Withdrawal, and Recovery Runbook
type: runbook
subtype: domain-release-recovery-procedure
version: v2
prior_version: v1
status: draft; repository-grounded; documentation-only; non-authoritative; non-executing; operational-rollback-held; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Habitat, release, rollback, correction, rights, sensitivity/geoprivacy, evidence, policy, review, security, and operations stewards"
created: 2026-05-12
updated: 2026-08-25
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
policy_label: public-review; habitat; rollback; withdrawal; correction-aware; rights-aware; sensitivity-aware; fail-closed; no-publication-authority
current_path: docs/runbooks/habitat/ROLLBACK_RUNBOOK.md
owning_root: docs/
responsibility: >-
  Explain how an authorized team should contain, evaluate, rehearse, hand off,
  verify, and audit a Habitat rollback or withdrawal without creating release
  authority, exposing sensitive ecological context, or confusing candidate
  validation with operational execution.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: >-
  Existing direct child of docs/runbooks/habitat/ and reconciled in place under
  the accepted docs/ responsibility root. This update creates no alias, mirror,
  migration, release-record home, rollback executor, or data-plane writer.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 434195e8727e6e8649fd6a9e7de06808c3e15261
  target_prior_blob: 1e91457758a83ec75b346ca9d8aa650c3fa9814d
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  rollback_card_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  rollback_card_schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  rollback_card_validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  rollback_card_tests_blob: c8aeac6348127fb768981e2b5b5588c6a7bdeb78
  synthetic_rehearsal_helper_blob: a8f6bff350e79b453f425ebce9a9ded6801f8944
  synthetic_rehearsal_tests_blob: b644ca6c4185b3f81bc339c077eae85299833261
  habitat_workflow_blob: 59771c027f688d7028a46c4635c0ec710b34e3ab
  habitat_candidate_index_blob: e55b9344cda673e069bce5525937f5a50666bf63
  ecoregions_candidate_index_blob: d8946a7181fe0f141a1ae43c28755baf54d28a1c
  habitat_fauna_candidate_index_blob: d5c3990bfdf8563721724d1e885022f28ba3f1df
  habitat_data_rollback_readme_blob: df4dcd37fda290b297435eb7254196e32fe1da68
  open_pull_requests_touching_target: 0
source_lineage:
  - "Google Drive: kfm_habitat_architecture_pdf_only_blueprint_2026-04-21.pdf — planning lineage; no current-repo proof"
  - "Google Drive: KFM_Habitat_Fauna_Thin_Slice_Extended_Pro_Blueprint.pdf — planning lineage; no current-repo proof"
related:
  - ../README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ../rollback-rehearsal.md
  - ../../domains/habitat/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../release/README.md
  - ../../../release/candidates/habitat/README.md
  - ../../../release/rollback_cards/README.md
  - ../../../release/correction_notices/README.md
  - ../../../release/withdrawal_notices/README.md
  - ../../../release/manifests/README.md
  - ../../../data/rollback/habitat/README.md
  - ../../../contracts/release/rollback_card.md
  - ../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../tools/validators/release/validate_rollback_card.py
  - ../../../tests/validators/test_validate_rollback_card.py
  - ../../../tools/release/rollback_apply.py
  - ../../../tests/release/test_synthetic_rollback_rehearsal.py
  - ../../../.github/workflows/domain-habitat.yml
tags: [kfm, habitat, runbook, rollback, withdrawal, correction, recovery, release, evidence, rights, sensitivity, geoprivacy, source-role, invalidation, synthetic-rehearsal]
notes:
  - "The prior edition was proposal-era, described this tracked path as unverified, linked nonexistent sibling files and stale schema names, and mixed candidate planning with operational rollback claims."
  - "The current shared RollbackCard profile is fixture-first, candidate-only, no-network, and non-executing."
  - "The current rollback helper is deterministic and synthetic-only; it never establishes production rollback authority."
  - "The governed Habitat candidate lane contains indexes only; bounded inspection established no non-README candidate record."
  - "The Habitat workflow executes one bounded synthetic land-cover materiality profile while explicitly holding Habitat proof production and release dry-run work."
  - "This document performs no containment, policy evaluation, review, lifecycle mutation, rollback, withdrawal, correction, release, deployment, promotion, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat — Rollback, Withdrawal, and Recovery Runbook

> **Use this runbook to prepare, validate, hand off, verify, and audit a governed recovery from a defective Habitat release.** This file explains the procedure; it is not release authority, a rollback executor, a public-state writer, an evidence resolver, a policy evaluator, or a publisher.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-posture)
[![RollbackCard: candidate only](https://img.shields.io/badge/RollbackCard-candidate%20only-8250df?style=flat-square)](#rollbackcard-candidate-contract)
[![Rehearsal: synthetic only](https://img.shields.io/badge/rehearsal-synthetic%20only-0969da?style=flat-square)](#synthetic-no-network-rehearsal)
[![Operational rollback: held](https://img.shields.io/badge/operational%20rollback-held-b42318?style=flat-square)](#current-repository-posture)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-negative-authority)

> [!IMPORTANT]
> **Current safe determination at `main@434195e8727e`: `HOLD — NO OPERATIONAL HABITAT ROLLBACK INSTANCE OR ACTIVE HABITAT RELEASE CANDIDATE IS ESTABLISHED`.** The repository contains a candidate-only `RollbackCard` contract, closed schema, no-network validator, fixtures, tests, and a synthetic rollback/withdrawal rehearsal helper. The governed Habitat candidate tree contains indexes but no non-README candidate record. The Habitat workflow explicitly holds proof production and release dry-run work. These controls do not prove an authorized production rollback path.

> [!CAUTION]
> A prior release, schema-valid `RollbackCard`, successful fixture test, synthetic alias switch, workflow result, pull request, merge, notice, or documentation update is not rollback authority. Operational rollback requires separately authenticated decision, policy, review, execution, invalidation, correction, and read-back evidence under an accepted release profile.

> [!WARNING]
> Habitat sensitivity is frequently **join-induced**. Do not place exact or reverse-engineerable rare-species, rare-plant, nest, den, roost, hibernaculum, spawning, breeding, stewardship, cultural, archaeological, private-land, infrastructure-adjacent, or restoration-priority detail in an ordinary issue, pull request, log, screenshot, notice draft, or rehearsal report. Use public-safe reason codes and restricted pointers.

**Quick navigation:** [Purpose](#purpose-and-scope) · [Placement](#placement-and-repository-fit) · [State](#current-repository-posture) · [Authority](#authority-and-negative-authority) · [Outcomes](#finite-outcomes-and-state-separation) · [Triggers](#recognized-triggers-and-containment) · [Preconditions](#preconditions-and-hard-stops) · [Candidate](#rollbackcard-candidate-contract) · [Decision](#choose-rollback-withdrawal-hold-or-forward-correction) · [Procedure](#authorized-execution-and-recovery-sequence) · [Invalidation](#invalidation-and-downstream-closure) · [Habitat controls](#habitat-specific-guardrails) · [Verification](#post-transition-verification) · [Rehearsal](#synthetic-no-network-rehearsal) · [Failures](#failure-states-and-escalation) · [Anti-patterns](#anti-patterns-to-refuse) · [Checklist](#operator-checklist) · [Open work](#open-verification-register) · [Evidence](#evidence-basis) · [Related](#related-surfaces) · [Document rollback](#document-change-rollback-and-non-effects)

---

<a id="purpose-and-scope"></a>

## Purpose and scope

This runbook answers one bounded recovery question:

> Given a specifically identified Habitat release-facing defect, what evidence, candidate record, review, containment, invalidation, execution handoff, and verification are required to restore a safe prior release, withdraw the affected release, hold action, or move to a forward correction without erasing history or exposing sensitive context?

### In scope

- Habitat release-facing artifacts and claims involving:
  - habitat patches, land-cover observations, and ecological systems;
  - habitat-quality and suitability outputs;
  - connectivity, corridor, restoration-opportunity, and stewardship derivatives;
  - uncertainty surfaces and ecoregion context layers;
  - public-safe map, API, export, search, graph, Evidence Drawer, and AI derivatives.
- Candidate preparation using the current shared `RollbackCard` profile.
- Containment and handoff requirements for an accountable release operation.
- Complete derivative-invalidation planning.
- Habitat-specific source-role, sensitivity, geoprivacy, time, model, and cross-lane checks.
- Deterministic synthetic rehearsal using the repository's marker-protected helper.

### Out of scope

This runbook does not:

- decide that a defect exists without admissible support;
- authenticate a reviewer, approver, operator, or steward;
- make rights, sovereignty, cultural, regulatory, ecological, legal, or land-management determinations;
- create or resolve evidence, policy, review, release, correction, or rollback authority;
- execute a production alias change, invalidation, deployment, release, or publication;
- mutate `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLETS`, or `PUBLISHED` by instruction alone;
- treat a map, model, tile, graph, summary, AI answer, or synthetic test as sovereign truth; or
- erase prior releases, receipts, proofs, decisions, corrections, or audit history.

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLETS -> PUBLISHED
```

Rollback is a governed transition away from a released state. It is not reverse promotion, a folder move, a hidden file copy, or deletion.

[Back to top](#top)

---

<a id="placement-and-repository-fit"></a>

## Placement and repository fit

### Directory Rules basis

The target is an existing human operational procedure:

```text
docs/runbooks/habitat/ROLLBACK_RUNBOOK.md
```

| Responsibility signature | Result |
|---|---|
| Artifact kind | Human runbook. |
| Authority owner | Documentation and operator guidance. |
| Responsibility root | `docs/`. |
| Domain scope | `habitat` as a segment inside the root, not a repository root. |
| Exposure | Public review documentation; sensitive operational detail remains elsewhere. |
| Mutability | Versioned replacement through review. |
| Placement outcome | `PLACE` — update the tracked file in place. |

Accepted ADR-0029 adopts Directory Rules v2 and makes `docs/doctrine/directory-rules.md` the writable placement authority. This same-path change does not create a new root, sibling authority, alias, mirror, schema home, policy home, release lane, rollback lane, or data store.

### Direct-dependency determination

The parent runbook index already recognizes recurring domain runbook packets. The local Habitat `README.md` is blank, but changing it would be a separate lane-index reconciliation with its own maturity inventory. No link, generator, manifest, schema, or code surface must change to make this same-path correction truthful. The dependency-closed slice is therefore this file only.

[Back to top](#top)

---

<a id="current-repository-posture"></a>

## Current repository posture

| Surface | Confirmed repository evidence | Bounded conclusion |
|---|---|---|
| Target runbook | Existing proposal-era file at blob `1e914577…` | Same-path modernization is warranted. |
| `RollbackCard` contract | Draft, schema-paired, fixture-first, non-executing | Defines candidate meaning only. |
| Schema and validator | Closed Draft 2020-12 profile plus deterministic no-network validation | Proves shape and local consistency only. |
| Candidate fixtures/tests | Three valid candidates, six invalid candidates, and expected findings | Proves fixture polarity; not decision or execution. |
| Synthetic helper/tests | Marker-protected deterministic `PLAN` and synthetic-only `--apply` | Proves isolated rehearsal behavior only. |
| Habitat candidate lane | Parent and two child indexes; no non-README candidate record found | No active Habitat release candidate is established. |
| Habitat data rollback lane | README and `.gitkeep` only | Data-plane support boundary exists; no release-specific rollback instance is established. |
| Habitat workflow | One bounded synthetic no-network land-cover materiality suite; proof and release jobs are explicit holds | No Habitat proof producer, release dry run, or rollback executor is admitted. |
| Operational release/rollback | No authenticated operator, current alias, accepted execution profile, invalidation adapters, or public read-back verified | Operational rollback remains `HOLD`. |

Differently named, unindexed, runtime-only, external, restricted, history-only, or locally deployed material remains `UNKNOWN` until directly verified. Absence from this bounded inventory is not a universal nonexistence claim.

[Back to top](#top)

---

<a id="authority-and-negative-authority"></a>

## Authority and negative authority

| Concern | Owning surface | This runbook may require | This runbook must not do |
|---|---|---|---|
| Release and rollback decision | Accepted records under `release/` plus accountable actors | Exact decision and scope pointers | Approve or execute a transition. |
| Candidate semantics | `contracts/release/rollback_card.md` | Conform candidate meaning to the contract | Redefine the object in prose. |
| Machine shape | Paired JSON Schema | Require schema-valid candidate input | Treat passing shape as approval. |
| Candidate validation | No-network validator and tests | Run the bounded fixture profile | Resolve evidence, authenticate actors, or mutate state. |
| Production execution | Accepted operator and runtime controls | Require exact version, authorization, and preconditions | Invent a command or assume the synthetic helper is production-ready. |
| Evidence and proof | Evidence/proof families and resolver | Require resolvable support | Manufacture evidence or proof. |
| Policy and review | Accepted policies, evaluator, and review records | Require finite decisions and obligations | Infer approval from a filename, label, or green check. |
| Correction/withdrawal notice | Release-accountability lanes | Require public-safe communication when applicable | Use notice prose as the decision itself. |
| Data-plane support | `data/rollback/habitat/` | Reference alias-revert and invalidation evidence when accepted | Store release decisions or treat it as a public API. |
| Public clients | Governed APIs and released public-safe carriers | Require resulting-state read-back | Direct clients to internal or unreleased stores. |

> [!NOTE]
> Emergency containment can disable exposure through an already-authorized operational control. Containment does not become a rollback decision, and this runbook does not establish the missing control or the actor allowed to use it.

[Back to top](#top)

---

<a id="finite-outcomes-and-state-separation"></a>

## Finite outcomes and state separation

The current candidate profile uses four dispositions:

| Candidate disposition | Meaning | Operational effect |
|---|---|---|
| `ROLLBACK_CANDIDATE` | Proposes restoring a distinct prior release. | None until separately authorized and executed. |
| `WITHDRAWAL_CANDIDATE` | Proposes withdrawal without selecting a prior release. | None until separately authorized and executed. |
| `HOLD` | Stops or delays action pending resolution. | Preserves fail-closed posture; no release mutation. |
| `ERROR` | Records invalid input or failed recovery evaluation. | No release mutation. |

Do not collapse these separate axes:

1. **Defect state** — suspected, confirmed, conflicted, or unresolved.
2. **Containment state** — not required, requested, active, verified, or failed.
3. **Candidate state** — absent, shape-valid, shape-invalid, or held.
4. **Policy state** — not evaluated, allow, deny, restrict, abstain, or error under the accepted policy vocabulary.
5. **Review state** — pending, complete, insufficient, rejected, or superseded.
6. **Execution state** — not authorized, authorized, started, completed, failed, or unknown under an accepted execution profile.
7. **Release state** — current, held, withdrawn, superseded, restored, or unknown under the accepted release model.
8. **Verification state** — pending, pass, fail, partial, or unknown.

A shape-valid candidate can coexist with denied policy, incomplete review, no execution authority, no public mutation, and a `HOLD` operational conclusion.

[Back to top](#top)

---

<a id="recognized-triggers-and-containment"></a>

## Recognized triggers and containment

The shared schema recognizes these public-safe trigger reason codes:

| Reason code | Habitat interpretation | Default handling |
|---|---|---|
| `RELEASE_DEFECT` | Released carrier or claim is incorrect or internally inconsistent. | Freeze scope; assess target and downstream effects. |
| `EVIDENCE_CONTRADICTION` | Evidence no longer supports a released Habitat claim. | Abstain or withdraw affected claim; do not improvise support. |
| `RIGHTS_CHANGE` | Terms, license, redistribution, or access posture changed. | Fail closed; involve rights steward. |
| `SENSITIVITY_DISCOVERY` | Released data or a join exposes protected ecological context. | Request immediate authorized containment; restrict incident detail. |
| `VALIDATION_FAILURE` | A released object fails an applicable validator. | Determine whether the target or shared profile is also affected. |
| `SOURCE_WITHDRAWAL` | Upstream source or steward withdrew support. | Evaluate withdrawal, supersession, and provenance obligations. |
| `POLICY_FAILURE` | Policy evaluation was missing, wrong, or bypassed. | Deny further use until accepted replay/review closes. |
| `SECURITY_ISSUE` | Exposure, tampering, or control failure affects the release. | Use the security incident route; keep public records non-sensitive. |
| `OPERATIONAL_FAILURE` | Serving, alias, cache, or invalidation behavior is defective. | Hold transition until state and concurrency can be verified. |
| `EMERGENCY_HOLD` | Immediate pause is required while facts remain incomplete. | Contain through authorized controls; do not claim rollback. |
| `INSUFFICIENT_EVIDENCE` | Support is inadequate to select a safe target. | `HOLD` or withdrawal; do not restore an unproved target. |
| `INPUT_INVALID` | Candidate input is malformed or internally inconsistent. | `ERROR`; correct input without touching release state. |

### Containment packet

Record only what is necessary and public-safe:

- affected release and carrier references;
- detected-at time and public-safe reason code;
- impacted domain/sublane and rough consequence class;
- containment request, actor, time, and result when an authorized control exists;
- restricted incident pointer for sensitive detail;
- candidate, evidence, policy, review, correction, withdrawal, and rollback pointers;
- known downstream consumers and invalidation classes; and
- current `HOLD`, `DENY`, `ABSTAIN`, or other finite posture.

Never paste protected geometry, redaction offsets, secret endpoints, credentials, exploit detail, private landowner information, or controlled source payloads into the public packet.

[Back to top](#top)

---

<a id="preconditions-and-hard-stops"></a>

## Preconditions and hard stops

Before preparing a rollback candidate, require:

- [ ] exact affected release reference, immutable manifest pointer, and expected digest;
- [ ] evidence that the affected state is current or release-facing;
- [ ] admissible support for the trigger and affected scope;
- [ ] source-role classification for every affected Habitat product;
- [ ] rights, sensitivity, geoprivacy, and public-safe geometry posture;
- [ ] complete downstream consumer and invalidation inventory;
- [ ] accountable review route and decision owner;
- [ ] correction and notice obligations;
- [ ] exact prior target when proposing rollback; and
- [ ] evidence that the target does not share the defect.

Stop with `HOLD`, `DENY`, or `ERROR` when any load-bearing condition is unresolved, including:

- affected release identity is ambiguous;
- target equals the affected release;
- target manifest, artifacts, or digests cannot be verified;
- target evidence does not resolve;
- target shares the same rights, sensitivity, policy, geometry, time, model, or source-role defect;
- review or separation of duties is required but unavailable;
- invalidation scope is incomplete;
- an active operation owns the same public state and concurrency is unresolved;
- the only available command is the synthetic rehearsal helper; or
- resulting public state cannot be read back through governed interfaces.

Do not treat a deadline, severity, feature value, or UI polish as compensation for a failed gate.

[Back to top](#top)

---

<a id="rollbackcard-candidate-contract"></a>

## `RollbackCard` candidate contract

The current candidate profile is `RollbackCard` schema version `1.0.0`. Every candidate carries:

- stable `id`, semantic `version`, and non-placeholder `spec_hash`;
- `disposition` and public-safe `trigger`;
- `affected_release_ref` and `target`;
- separate evidence, policy, and review references;
- optional correction notice reference as allowed by the profile;
- one or more invalidation classes;
- restoration requirements;
- decision/effective timing;
- supersession lineage; and
- explicit governance non-authority flags.

The candidate schema requires all governance flags to remain false and `release_ref` to remain null. A candidate therefore cannot claim that authority was created, policy was evaluated, review completed, rollback executed, or public state mutated.

### Bounded validation

```bash
python tools/validators/release/validate_rollback_card.py --fixtures

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
```

A green result proves only schema shape, local cross-field consistency, fixture polarity, duplicate-key rejection, nonfinite-number rejection, canonical arrays, target/disposition agreement, time ordering, non-self-supersession, and governance-boundary enforcement.

It does **not**:

- resolve references;
- authenticate an actor or signature;
- determine that a prior release is safe;
- execute policy or review;
- change an alias or cache;
- emit an operational receipt;
- execute rollback, withdrawal, correction, release, deployment, or publication.

[Back to top](#top)

---

<a id="choose-rollback-withdrawal-hold-or-forward-correction"></a>

## Choose rollback, withdrawal, hold, or forward correction

| Condition | Correct candidate posture | Why |
|---|---|---|
| A distinct prior release is verified safe and complete | `ROLLBACK_CANDIDATE` | A bounded restoration target exists. |
| No safe prior release exists, but the affected release must leave current use | `WITHDRAWAL_CANDIDATE` | Withdrawal is safer than restoring a defective target. |
| Facts, authority, policy, review, target safety, or concurrency remain unresolved | `HOLD` | Fail closed without pretending recovery is complete. |
| Candidate input is malformed or internally inconsistent | `ERROR` | No action should be derived from invalid input. |
| A corrected new release is required because every prior target shares the defect | Forward correction/supersession through the release process | Rollback cannot safely solve the defect. |

> [!IMPORTANT]
> Never roll back to the most recent prior release merely because it exists. A rollback target must be independently checked against the defect, evidence, rights, sensitivity, source role, policy, review, integrity, correction, and public-safe obligations that matter to the affected scope.

[Back to top](#top)

---

<a id="authorized-execution-and-recovery-sequence"></a>

## Authorized execution and recovery sequence

The repository does not currently establish an accepted production Habitat rollback operator. The sequence below is therefore an **operator contract and handoff**, not a runnable production command list.

1. **Freeze authority and state.** Pin repository revision, affected release, manifest, carrier identities, public read-back, candidate profile, and applicable policies.
2. **Classify and contain.** Record a safe reason code and request authorized containment when consequence requires it. Verify containment separately.
3. **Map impact.** Enumerate Habitat carriers, cross-lane derivatives, caches, tiles, catalogs, triplets, search/vector indexes, Evidence Drawer payloads, AI outputs, exports, and notices.
4. **Select a disposition.** Choose rollback, withdrawal, hold, error, or forward correction using the table above.
5. **Verify target.** For rollback, verify a distinct prior release, exact manifest/artifact digests, evidence closure, rights, sensitivity, policy, review, and public-safe representation.
6. **Create candidate records.** Prepare a schema-valid `RollbackCard` and required correction/withdrawal notice drafts. Candidate creation has no public effect.
7. **Run bounded checks.** Validate candidate shape and, where useful, rehearse the scenario in a synthetic marker-protected root.
8. **Obtain accountable decisions.** Require authenticated policy and human review appropriate to consequence, including independent review where required.
9. **Prepare execution envelope.** Bind exact before-state, expected after-state, concurrency guard, accepted operator version, invalidation plan, stop conditions, and receipt targets.
10. **Execute only through accepted machinery.** The production operator, authorization model, and execution receipt remain `HOLD`; do not substitute `tools/release/rollback_apply.py`.
11. **Invalidate and rebuild.** Close every affected derived carrier and regenerate only from the resulting governed state.
12. **Verify read-back.** Confirm the resulting release state and public-safe behavior through governed APIs and released carriers.
13. **Close visibly.** Link decisions, receipts, notices, changelog, supersession, failures, and remaining holds without erasing prior history.

If step 10 lacks accepted machinery, stop after handoff with `HOLD`. Documentation must not turn an implementation gap into an ad hoc production command.

[Back to top](#top)

---

<a id="invalidation-and-downstream-closure"></a>

## Invalidation and downstream closure

The candidate schema recognizes these classes:

| Invalidation class | Habitat examples | Closure evidence needed |
|---|---|---|
| `API_CACHE` | Habitat feature, Evidence Drawer, and lookup responses | Cache purge/rebind receipt and governed read-back. |
| `CDN` | Public-safe tiles, exports, and static metadata | Purge result and digest/header verification. |
| `TILES` | PMTiles, MVT, raster, terrain, previews | Manifest/digest parity and visual/data read-back. |
| `CATALOG` | Habitat catalog and layer discovery entries | Catalog points only to resulting released state. |
| `TRIPLETS` | Habitat relationships and cross-domain projections | Affected edges invalidated or rebuilt with lineage. |
| `SEARCH_INDEX` | Habitat names, summaries, places, and snippets | Removed/superseded records no longer resolve as current. |
| `VECTOR_INDEX` | Evidence retrieval or semantic-search derivatives | Withdrawn chunks removed or rebound to current evidence. |
| `AI_CACHE` | Focus Mode answers, summaries, and citations | Affected outputs invalidated; unsupported answers abstain or deny. |
| `DOWNSTREAM_DERIVATIVES` | Reports, stories, screenshots, exports, dashboards, analytics | Consumer-by-consumer closure or explicit hold. |

Invalidation is not proved by listing a class. Each class requires an owner, affected identifiers, accepted adapter or manual control, execution evidence, and read-back. Unknown consumers remain a hold when their stale output could cause material harm.

[Back to top](#top)

---

<a id="habitat-specific-guardrails"></a>

## Habitat-specific guardrails

### Source-role anti-collapse

Keep these roles distinct during recovery:

- regulatory critical-habitat designation;
- observed land-cover or ecological measurement;
- modeled habitat or suitability output;
- aggregate or classification surface;
- administrative or stewardship context;
- synthetic fixture; and
- derived occurrence-to-habitat assignment.

Modeled habitat must not be restored under a regulatory role. Suitability is not occurrence. Ecoregion context is not species presence, habitat quality, legal designation, hydrologic truth, soil truth, parcel truth, or title truth.

### Sensitive and join-induced exposure

A public-safe Habitat layer can become sensitive when joined with Fauna, Flora, stewardship, archaeology, land, or infrastructure detail. Check the full join and all side channels:

- geometry and attributes;
- labels, popups, and tooltips;
- search snippets and exports;
- tiles and browser caches;
- graph edges and vector chunks;
- screenshots and story snapshots; and
- generated summaries and AI answers.

Style-only hiding is not a safety control. Sensitive geometry must be transformed, generalized, delayed, redacted, staged, or denied before public delivery. Preserve transform receipts and reasons where an accepted profile exists.

### Model and representation integrity

For suitability, connectivity, restoration, and uncertainty products, verify:

- model/input/version identity;
- spatial and temporal scope;
- uncertainty and limitations;
- distinction between source observation and derived output;
- representation/generalization transforms; and
- whether the target release is reproducible from retained inputs and receipts.

A visually plausible map is not evidence that the target is safe.

### Time and freshness

Keep observed, valid, source, retrieval, processing, release, effective, correction, and transaction times distinct. A rollback can restore prior bytes while still creating stale or misleading public state. Mark stale, restrict, withdraw, or move to forward correction when temporal support is no longer fit.

### Cross-lane coordination

| Related lane | Habitat recovery effect | Required posture |
|---|---|---|
| Fauna | Habitat assignments and occurrence-linked views may reference the affected release | Notify Fauna owner; preserve occurrence authority and geoprivacy. |
| Flora | Community or rare-plant context may create sensitive joins | Notify Flora owner; preserve Flora authority and public-safe transforms. |
| Soil/Hydrology | Substrate, moisture, wetlands, and riparian derivatives may depend on Habitat outputs | Invalidate only dependent derivatives; do not rewrite source truth. |
| Hazards/Atmosphere | Fire, drought, flood, smoke, and resilience views may carry stale Habitat inputs | Rebind or hold affected views with explicit time/source roles. |
| Agriculture | Land-cover and suitability comparisons may consume Habitat carriers | Preserve agriculture/habitat distinction and invalidate derived comparisons. |
| Archaeology/People/Land | Joins may reveal steward-controlled, cultural, private-land, or ownership context | Fail closed and use the owning sensitivity/rights process. |

A Habitat rollback may notify and invalidate dependencies; it must not silently mutate another lane's canonical content.

[Back to top](#top)

---

<a id="post-transition-verification"></a>

## Post-transition verification

Operational closure requires evidence for every applicable item:

- [ ] exact affected and resulting release identities are recorded;
- [ ] affected history, manifests, artifacts, receipts, proofs, reviews, and corrections remain inspectable;
- [ ] resulting manifest and artifact digests match expected state;
- [ ] `EvidenceRef` values resolve to admissible `EvidenceBundle` support;
- [ ] rights, sensitivity, source-role, time, model, and representation obligations are satisfied;
- [ ] accountable policy and review records cover the exact scope;
- [ ] correction, withdrawal, supersession, and public notice records agree with release state;
- [ ] all applicable invalidation classes have execution evidence and read-back;
- [ ] cross-lane consumers no longer treat the affected release as current;
- [ ] governed APIs, maps, exports, Evidence Drawer, and AI surfaces reflect the resulting state;
- [ ] unsupported AI answers return the applicable abstain/deny/error posture;
- [ ] no public client reaches internal, quarantined, candidate, or direct-model stores; and
- [ ] unresolved failures remain visible as `HOLD`, `DENY`, `ABSTAIN`, or `ERROR` rather than being hidden.

A completed alias change without these checks is an incomplete recovery, not a successful rollback.

[Back to top](#top)

---

<a id="synthetic-no-network-rehearsal"></a>

## Synthetic no-network rehearsal

The shared helper is deliberately safe by construction:

- it requires a root containing `.kfm-synthetic-rollback-rehearsal` with `synthetic-only` content;
- it requires `synthetic: true` in the scenario;
- it defaults to no-write `PLAN` mode;
- `--apply` mutates only the marker-protected synthetic root;
- it verifies alias/manifest/artifact digests and complete invalidation classes;
- it retains affected release bytes and append-only correction lineage; and
- its report declares that no authority, policy, review, release, publication, or public mutation is created.

Run the focused test suite:

```bash
python -m unittest -q tests.release.test_synthetic_rollback_rehearsal
```

Plan an already prepared synthetic scenario:

```bash
python tools/release/rollback_apply.py \
  --workspace <marker-protected-synthetic-root> \
  --scenario <synthetic-scenario.json>
```

Do not point the helper at repository lifecycle lanes, a deployed environment, real release storage, production aliases, or public caches. Do not remove or bypass the marker or `synthetic: true` guard. A passing rehearsal is implementation evidence for the synthetic profile only.

[Back to top](#top)

---

<a id="failure-states-and-escalation"></a>

## Failure states and escalation

| Failure | Finite posture | Recovery path |
|---|---|---|
| Candidate JSON invalid, duplicate-keyed, nonfinite, or inconsistent | `ERROR` | Correct input; rerun bounded validator; no release action. |
| Target absent, same as affected, or digest-mismatched | `HOLD` | Identify and verify a distinct target or choose withdrawal/forward correction. |
| Evidence missing or contradictory | `ABSTAIN` / `HOLD` | Withdraw unsupported claims or rebuild support through evidence governance. |
| Rights or sensitivity unresolved | `DENY` / `HOLD` | Contain through authorized controls; complete accountable review. |
| Target shares defect | `HOLD` | Do not restore; choose withdrawal or forward correction. |
| Review insufficient or actor unauthenticated | `HOLD` | Obtain required review and separation of duties. |
| Invalidation incomplete | `HOLD` | Expand inventory, execute missing closures, and verify read-back. |
| Synthetic helper receives non-synthetic input or unsafe root | `ERROR` / helper denial | Preserve guard; use no production workaround. |
| Operational executor or receipt profile absent | `HOLD` | Commission and review a separate implementation slice. |
| Public read-back differs from expected state | `ERROR` / `HOLD` | Recontain affected surfaces; reconcile alias, caches, manifests, and consumers. |

Escalate sensitive incidents through restricted channels. Public records should carry only safe classifications, status, and governed pointers.

[Back to top](#top)

---

<a id="anti-patterns-to-refuse"></a>

## Anti-patterns to refuse

| Anti-pattern | Why it fails | Correct posture |
|---|---|---|
| Hidden file copy or directory move as rollback | Bypasses release, evidence, policy, review, correction, and read-back | Use governed release recovery and retain history. |
| Silent edit of a published Habitat claim | Erases correction lineage | Issue explicit correction, withdrawal, supersession, or rollback records. |
| Treating schema-valid candidate as approved | Candidate governance flags explicitly remain false | Obtain separate accountable decisions. |
| Using the synthetic helper on real state | Violates its marker-protected non-authority boundary | Stop; commission accepted production machinery. |
| Restoring the nearest prior release without target review | Prior state may share the defect | Verify target independently or withdraw/correct forward. |
| Style-only hiding of sensitive geometry | Sensitive bytes still ship | Transform or deny before delivery and close side channels. |
| Treating suitability as occurrence or modeled habitat as regulatory designation | Collapses source roles | Restore role-correct state and visible limitations. |
| Invalidating only the map | Search, graph, export, vector, AI, and cache surfaces stay stale | Close all applicable invalidation classes. |
| AI-drafted explanation used as evidence or approval | Generated language is interpretive | Resolve evidence and review independently. |
| Deleting prior release artifacts to “clean up” | Destroys audit and rollback lineage | Retain immutable history unless a separate lawful erasure process applies. |

[Back to top](#top)

---

<a id="operator-checklist"></a>

## Operator checklist

### Intake and containment

- [ ] Repository, target, affected release, and public read-back are pinned.
- [ ] Trigger uses a supported public-safe reason code.
- [ ] Sensitive detail is restricted and absent from public artifacts.
- [ ] Authorized containment is requested and independently verified when needed.
- [ ] Incident, correction, withdrawal, and review pointers are recorded.

### Candidate and review

- [ ] Disposition matches the facts.
- [ ] Rollback target is distinct and independently verified safe.
- [ ] Candidate arrays are complete, sorted, and unique.
- [ ] Required evidence, policy, review, and correction references are present.
- [ ] Governance flags remain false in the candidate.
- [ ] Bounded validator/tests pass, with their limits recorded.
- [ ] Accountable policy and human review occur outside candidate validation.

### Execution handoff and closure

- [ ] Complete invalidation scope and owners are recorded.
- [ ] Exact before-state, expected after-state, concurrency guard, and stop conditions are frozen.
- [ ] Accepted executor and execution/alias-revert receipt profiles are identified.
- [ ] Execution stops if production machinery is not accepted.
- [ ] Resulting manifest, artifacts, evidence, policy, review, rights, sensitivity, and source-role checks pass.
- [ ] Every affected public and derived surface is verified or transparently held.
- [ ] Prior history remains inspectable and no claim exceeds the evidence.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| Item | Current status | Required evidence before operational reliance |
|---|---|---|
| Accountable Habitat/release/rollback/correction stewards | `NEEDS VERIFICATION` | Named roles, permissions, review scope, and escalation route. |
| Independent review and separation of duties | `NEEDS VERIFICATION` | Enforced reviewer/approver model for consequence classes. |
| Production Habitat release identity and alias | `UNKNOWN` | Accepted manifest instance, current pointer, resolver, and authenticated read-back. |
| Operational rollback/withdrawal executor | `HOLD` | Accepted contract, implementation, authorization, negative tests, concurrency controls, and receipt. |
| Cache/tile/catalog/search/vector/AI invalidation adapters | `UNKNOWN` | Implemented adapters, ownership, deterministic tests, and read-back evidence. |
| Habitat proof producer and evidence closure | `HOLD` | Accepted producer, schemas, public-safe fixtures, resolver, access controls, receipts, and workflow. |
| Habitat release dry run | `HOLD` | Active candidate identity, accepted candidate/manifest profile, independent review, and fail-closed command. |
| Active Habitat source authority and policy | `HOLD` / `NEEDS VERIFICATION` | Admitted sources, rights/sensitivity decisions, accepted policy evaluator, and source-role validation. |
| First real Habitat candidate or release | Not established | Non-README candidate, immutable artifacts, review, decision, manifest, released carrier, and read-back. |
| Habitat runbook lane README | Blank | Repository-grounded lane boundary, child maturity, owners, and navigation. |
| Sibling no-network and promotion runbooks | Proposal-era at the pinned base | Separate same-path reconciliation; do not infer their commands or maturity here. |
| Public notice delivery | `NEEDS VERIFICATION` | Accepted correction/withdrawal notice workflow and parity with release state. |
| Sensitive-detail incident handling | `NEEDS VERIFICATION` | Restricted reporting system, access controls, retention, redaction, and correction process. |

These gaps do not prevent this documentation correction. They prevent an unqualified claim that Habitat rollback is operationally ready.

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

### Current repository evidence

| Evidence | What it supports | What it does not prove |
|---|---|---|
| Accepted ADR-0029 and Directory Rules v2 | Same-path placement and responsibility-root separation | Release authority or runtime behavior. |
| Current target and neighboring runbooks | Proposal-era drift and existing packet placement | Correctness of unverified commands or routes. |
| `contracts/release/rollback_card.md` | Candidate semantics and non-authority boundary | Operational decision or execution. |
| Paired schema, validator, fixtures, and tests | Closed shape, finite vocabularies, fixture polarity, local consistency | Reference resolution, signatures, policy, review, target safety, or mutation. |
| Synthetic helper and tests | Marker-protected no-network rehearsal behavior | Production alias, live invalidation, or release readiness. |
| Habitat candidate indexes | Current lane and no non-README candidate in bounded inspection | Universal absence of all Habitat material elsewhere. |
| Habitat data rollback README | Conservative data-plane support and sensitivity boundary | Accepted release-specific instance or execution receipt. |
| `domain-habitat` workflow | Bounded materiality suite and explicit proof/release holds | Habitat truth, evidence closure, release, or rollback. |

### Google Drive planning lineage

| Source | Retained contribution | Evidence limit |
|---|---|---|
| `kfm_habitat_architecture_pdf_only_blueprint_2026-04-21.pdf` | Habitat object boundaries, source-role anti-collapse, sensitive joins, public-safe geometry, rollback/correction planning, and lifecycle doctrine | It explicitly found no mounted repository; paths and implementations are planning lineage. |
| `KFM_Habitat_Fauna_Thin_Slice_Extended_Pro_Blueprint.pdf` | Derived habitat-assignment boundary, public-safe occurrence handling, evidence/provenance, rollback references, and no-network posture | It is plan-only and does not establish a current source, candidate, release, API, workflow, or publication path. |

Current repository evidence outranks planning documents for implementation behavior. Planning lineage remains useful where its domain distinctions agree with current authority.

[Back to top](#top)

---

<a id="related-surfaces"></a>

## Related surfaces

### Runbooks and Habitat documentation

- [`docs/runbooks/README.md`](../README.md) — parent operational-procedure boundary.
- [`docs/runbooks/habitat/NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) — proposal-era no-network procedure; reconcile separately.
- [`docs/runbooks/habitat/PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) — proposal-era promotion procedure; reconcile separately.
- [`docs/runbooks/habitat/SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) — repository-grounded source-head inspection and handoff procedure.
- [`docs/runbooks/rollback-rehearsal.md`](../rollback-rehearsal.md) — shared synthetic rehearsal explanation.
- [`docs/domains/habitat/README.md`](../../domains/habitat/README.md) — Habitat scope and domain language.

### Governing and release surfaces

- [Directory Rules v2](../../doctrine/directory-rules.md).
- [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md).
- [`release/README.md`](../../../release/README.md).
- [`release/candidates/habitat/README.md`](../../../release/candidates/habitat/README.md).
- [`release/rollback_cards/README.md`](../../../release/rollback_cards/README.md).
- [`release/correction_notices/README.md`](../../../release/correction_notices/README.md).
- [`release/withdrawal_notices/README.md`](../../../release/withdrawal_notices/README.md).
- [`release/manifests/README.md`](../../../release/manifests/README.md).
- [`data/rollback/habitat/README.md`](../../../data/rollback/habitat/README.md).

### Contract, validator, and rehearsal implementation

- [`contracts/release/rollback_card.md`](../../../contracts/release/rollback_card.md).
- [`schemas/contracts/v1/release/rollback_card.schema.json`](../../../schemas/contracts/v1/release/rollback_card.schema.json).
- [`tools/validators/release/validate_rollback_card.py`](../../../tools/validators/release/validate_rollback_card.py).
- [`tests/validators/test_validate_rollback_card.py`](../../../tests/validators/test_validate_rollback_card.py).
- [`tools/release/rollback_apply.py`](../../../tools/release/rollback_apply.py).
- [`tests/release/test_synthetic_rollback_rehearsal.py`](../../../tests/release/test_synthetic_rollback_rehearsal.py).
- [`.github/workflows/domain-habitat.yml`](../../../.github/workflows/domain-habitat.yml).

[Back to top](#top)

---

<a id="document-change-rollback-and-non-effects"></a>

## Document change rollback and non-effects

### Rollback of this repository documentation change

Before merge, close or abandon the draft pull request and leave `main` unchanged.

After merge, use a transparent revert or a smaller reviewed forward correction against the actual merged commit. Do not rewrite shared history, and preserve later independent edits.

The prior documentation blob is:

```text
1e91457758a83ec75b346ca9d8aa650c3fa9814d
```

Restoring that blob would restore proposal-era documentation only. It would not alter source, evidence, policy, review, lifecycle, release, alias, cache, artifact, correction, withdrawal, rollback, deployment, or publication state.

### Non-effects of this runbook update

This update does not:

- create a Habitat release or candidate;
- validate a real target release;
- create a `RollbackCard`, `CorrectionNotice`, `WithdrawalNotice`, `ReleaseManifest`, or execution receipt;
- admit or activate a Habitat source;
- evaluate policy or complete review;
- execute a synthetic or production rollback;
- invalidate caches, tiles, catalogs, indexes, graphs, vectors, AI outputs, or derivatives;
- change an alias, lifecycle state, deployed service, public map, API, or published carrier;
- release, deploy, promote, publish, correct, withdraw, or roll back anything; or
- change repository settings, protections, secrets, environments, or permissions.

[Back to top](#top)
