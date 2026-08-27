<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/hazards/readme
title: Hazards Runbooks · Lane Boundary and Navigation
type: readme
subtype: domain-runbook-lane-boundary
version: v1.0.0
status: DRAFT_REPOSITORY_GROUNDED; DOCUMENTATION_ONLY; MIXED_CHILD_OPERATIONAL_MATURITY; BOUNDED_SYNTHETIC_VALIDATION_AND_REHEARSAL; LIVE_OPERATIONS_HELD; NOT_FOR_LIFE_SAFETY; NON_RELEASE; NON_PUBLICATION
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Accountable Hazards, source, scientific, evidence, policy, rights, sensitivity, emergency-management, accessibility, review, promotion, release, correction, rollback, operations, and independent-review assignments remain NEEDS VERIFICATION."
created: 2026-08-27
updated: 2026-08-27
policy_label: repository-facing; hazards; runbook-index; mixed-maturity; fail-closed; not-for-life-safety; non-publisher
current_path: docs/runbooks/hazards/README.md
owning_root: docs/
responsibility: "Define the human-facing Hazards runbook lane boundary, disclose current child maturity, and route an operator or reviewer to the narrowest applicable procedure without creating source, evidence, policy, review, lifecycle, release, deployment, rollback-execution, or publication authority."
truth_posture: cite-or-abstain
authority_class: explanatory operational-documentation index
authority_effect: none
source_activation_effect: none
lifecycle_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  upstream_base_ref: main
  upstream_base_commit: 1ed2fb58cc499cb5c2536ab1f3e46cf9cd1a3912
  stacked_base_ref: automation/markdown-hazards-source-refresh-runbook-20260827
  stacked_base_commit: 832e3100829f516928e1178687770a7faf192e4c
  dependency_pull_request: 3648
  target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  not_for_life_safety_audit_blob: e75233042dc69da67f9931a6b056aedb46a21861
  no_network_test_blob: 0b7b3c5bd71c502bef2bf3529b9d379272e5f10a
  promotion_runbook_blob: cb420415cea6f1a43c70fbba1604c06fc031b5de
  rollback_drill_blob: 4e45184ae99c934d577372f6503f9ede5880d95f
  rollback_runbook_blob: 624e86620bdd09faae7f64044222ee709717d15c
  source_refresh_runbook_blob_on_stacked_base: 9e998e5e792eb2c2df542e2ebd4afd60a6ee6af2
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  child_runbook_count: 6
  substantive_children_on_stacked_base: 6
  placeholder_children_on_stacked_base: 0
source_lineage:
  - title: kfm_hazards_extended_pro_pdf_only_blueprint.pdf
    source_class: PLANNING_LINEAGE
    use: not-for-life-safety, source-role, temporal, evidence, offline-first, correction, and rollback framing only
  - title: Track runbook inventory reconciliation
    source_class: NOTION_COORDINATION_ONLY
    use: identifies the one-byte Hazards lane README as the next documentation-boundary gap
  - title: KFM Markdown Update & Modernization Agent v1.0
    source_class: CURRENT_TASK_GUIDANCE
    use: same-path repository-grounded Markdown modernization and focused draft-pull-request delivery
related:
  - docs/runbooks/README.md
  - docs/domains/hazards/README.md
  - docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - .github/workflows/domain-hazards.yml
  - .github/workflows/rollback-drill.yml
  - policy/domains/hazards/README.md
  - release/README.md
  - release/candidates/hazards/README.md
notes:
  - "This README is stacked on PR #3648 so its source-refresh entry describes that branch's repository-grounded v2 procedure rather than the proposal-era file still present on upstream main at branch creation."
  - "All six child procedures are substantive repository-grounded drafts on the stacked base, but only bounded synthetic validation and marker-protected rollback rehearsal are executable with current evidence."
  - "No standalone Hazards correction, release, validation, or stale-state runbook is tracked in this directory; existing procedures and owning responsibility roots remain the current routes until a separately grounded need justifies another file."
  - "This documentation change creates no source admission, evidence, policy, review, lifecycle, release, deployment, promotion, rollback-execution, publication, or public-state effect."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hazards Runbooks

> Human-facing navigation for inspecting, validating, refreshing, containing, correcting, rehearsing, and preparing accountable review handoffs for the Hazards lane. These documents explain procedures; they do not create authority or operational state.

> [!IMPORTANT]
> **A runbook is not an authority object.** A tracked file, complete checklist, passing fixture, green workflow, pull request, merge, readiness result, or rehearsal report is not source admission, an `EvidenceBundle`, policy approval, completed review, lifecycle promotion, release authorization, deployment, rollback execution, or publication.

> [!WARNING]
> **KFM Hazards is not an emergency-alerting system, incident-command system, medical service, regulatory authority, or substitute for official instructions.** KFM may preserve evidence-linked historical, regulatory, observed, modeled, exposure, resilience, and time-bounded operational context. It must not originate, replace, delay, retract, summarize as actionable, or interpret a warning, evacuation order, shelter instruction, medical direction, all-clear, or other life-safety message. Direct urgent needs to the appropriate official authority.

> [!CAUTION]
> **Current disposition: `SUBSTANTIVE_DOCUMENTATION / BOUNDED_SYNTHETIC_VALIDATION_AND_REHEARSAL / LIVE_OPERATIONS_HOLD`.** On the stacked base, all six child runbooks are substantive repository-grounded drafts. The implemented evidence is narrower: committed drought fixtures and deterministic U.S. Drought Monitor materiality validation, plus a marker-protected synthetic rollback and withdrawal rehearsal. Live source refresh, active policy enforcement, EvidenceBundle and proof closure, candidate assembly, promotion execution, operational rollback, release, deployment, public read-back, and publication remain held, absent, unknown, or in need of verification.

> [!NOTE]
> **Stacked delivery dependency.** This README is based on [PR #3648](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/3648), which modernizes `SOURCE_REFRESH_RUNBOOK.md`. Until that dependency is merged or this change is rebased and reconciled, upstream `main` does not contain the source-refresh maturity described here.

**Quick navigation:** [Lane boundary](#lane-boundary) · [Choose a procedure](#choose-the-narrowest-procedure) · [Child maturity](#current-child-maturity) · [Capability map](#current-capability-and-hold-map) · [Invariants](#shared-hazards-operating-invariants) · [Sequencing](#procedure-sequencing-and-state-separation) · [Validation](#validation-and-rehearsal-entry-points) · [Stops](#mandatory-stop-conditions) · [Handoff](#authority-ownership-and-handoff) · [Gaps](#open-verification-and-missing-procedures) · [Related](#related-responsibility-surfaces) · [Maintenance](#maintenance-correction-and-document-rollback)

---

<a id="lane-boundary"></a>

## Lane boundary

`docs/runbooks/hazards/` owns human procedures for Hazards work. It does not own source admission, domain meaning, machine shape, evidence, policy, review decisions, lifecycle instances, release records, runtime behavior, or public carriers.

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and the adopted [Directory Rules v2](../../doctrine/directory-rules.md) place these responsibilities in separate roots:

| Concern | Owning surface | Role of this README and its children |
|---|---|---|
| Human operating procedure | `docs/runbooks/hazards/` | Explain preconditions, commands, outcomes, stops, records, and handoff |
| Hazards meaning and domain boundary | `contracts/domains/hazards/` and [`docs/domains/hazards/`](../../domains/hazards/) | Link and consume; do not redefine |
| Machine shape | `schemas/contracts/v1/domains/hazards/` and applicable release schemas | Require validation; do not treat shape validity as truth or approval |
| Synthetic examples and executable behavior | `fixtures/`, `tests/`, `tools/`, pipelines, connectors, scripts, and workflows according to responsibility | Point to exact entry points and bound what their results prove |
| Source identity and activation | Source descriptors, source-authority controls, and accepted activation decisions | Inspect exact authority; do not activate a source from Markdown |
| Evidence, receipts, proofs, and lifecycle objects | Governed `data/` lanes and their contracts | Resolve and record; do not manufacture or collapse object families |
| Allow, deny, abstain, restrict, or hold | `policy/` plus governed evaluation and review | Explain how to obtain and respond to a finite result; do not invent one |
| Promotion, release, correction, withdrawal, and rollback | `release/` and linked accountability objects | Prepare or rehearse a handoff; do not approve or execute a transition |
| Public delivery | Governed APIs and released public-safe carriers | Verify the declared boundary; do not expose internal or unreleased stores |

The canonical lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A procedure may describe a state transition. Documentation presence, validation success, or a file move cannot perform it.

[Back to top](#top)

---

<a id="choose-the-narrowest-procedure"></a>

## Choose the narrowest procedure

Start with the procedure whose terminal boundary matches the immediate question. Do not use a later-stage runbook to bypass missing earlier authority or support.

| Need | Procedure | Highest bounded result | Terminal boundary |
|---|---|---|---|
| Audit whether wording, a map, API, UI, AI answer, export, report, or other surface stays outside life-safety authority | [`NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md`](NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md) | Public-safe audit finding and accountable-review handoff | Documentary audit only; runtime enforcement and any exception authority remain unverified |
| Run the current deterministic Hazards fixture checks without live source access | [`NO_NETWORK_TEST_RUNBOOK.md`](NO_NETWORK_TEST_RUNBOOK.md) | `BOUNDED_SYNTHETIC_VALIDATION_PASS` | Committed drought-family and USDM materiality profiles only; no source, proof, release, or publication effect |
| Assess or prepare a refresh of an already proposed or admitted Hazards source | [`SOURCE_REFRESH_RUNBOOK.md`](SOURCE_REFRESH_RUNBOOK.md) | `SOURCE_REFRESH_PREFLIGHT_COMPLETE`, bounded validation, or implementation-review handoff | No live fetch, source activation, lifecycle write, evidence/proof assembly, release, or publication |
| Assess whether a specific immutable Hazards candidate is ready for accountable release review | [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) | `READY_FOR_ACCOUNTABLE_RELEASE_REVIEW` | Preflight and handoff only; no promotion, release, deployment, or public write |
| Rehearse the implemented marker-protected synthetic rollback and withdrawal mechanics | [`ROLLBACK_DRILL.md`](ROLLBACK_DRILL.md) | `SYNTHETIC_REHEARSAL_PASS` | Temporary synthetic roots only; no real candidate, alias, cache, release, or public recovery |
| Contain and classify a released or release-facing Hazards defect and decide among rollback, withdrawal, forward correction, or hold | [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Decision record and accountable operational handoff supported by current evidence | Operational planning, authorization, execution, invalidation, alias mutation, and public recovery remain held |

When several procedures apply, preserve their state boundaries. A common order is:

```text
not-for-life-safety audit
  -> source or candidate preflight
  -> bounded no-network validation
  -> accountable review handoff
  -> separately governed decision and transition
  -> correction / withdrawal / rollback assurance
```

The order is not permission. Every step still requires the authority, evidence, inputs, and environment named by its own procedure.

[Back to top](#top)

---

<a id="current-child-maturity"></a>

## Current child maturity

The table below describes repository documents on stacked base `832e3100829f516928e1178687770a7faf192e4c`. It does not prove a live source, accepted policy, authenticated reviewer, released artifact, deployed service, or public carrier.

| Procedure | Current document maturity | Confirmed or bounded capability | Material hold |
|---|---|---|---|
| [`NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md`](NOT_FOR_LIFE_SAFETY_AUDIT_RUNBOOK.md) | Substantive repository-grounded draft | Change-impact classes, fail-closed semantic audit, source/time/referral review, workflow-safety preflight, and public-safe handoff | Complete runtime/API/UI/AI enforcement and accountable safety/legal review remain unverified |
| [`NO_NETWORK_TEST_RUNBOOK.md`](NO_NETWORK_TEST_RUNBOOK.md) | Substantive repository-grounded draft | Three drought-family schema/fixture profiles, in-process network-denial checks, deterministic USDM materiality tests, and exact focused commands | Live source access, broader hazard families, EvidenceBundle resolution, active policy, proof, candidate assembly, release, deployment, and publication remain held |
| [`SOURCE_REFRESH_RUNBOOK.md`](SOURCE_REFRESH_RUNBOOK.md) | Substantive repository-grounded draft on dependency PR #3648 | Exact source/connector/pipeline preflight plus the current no-network fixture and materiality validation routes | Source-authority register is empty and projection-only; descriptors, connectors, watcher, and pipeline remain placeholder, conflicted, or unverified; live refresh is held |
| [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) | Substantive repository-grounded draft | Bounded no-network candidate-readiness checks and a finite review handoff model | Hazards candidate is absent; policy runtime, accountable release authority, operational promotion, release, deployment, and publication remain held |
| [`ROLLBACK_DRILL.md`](ROLLBACK_DRILL.md) | Substantive repository-grounded bounded drill | Eight generic and four Hazards-focused tests against temporary marker-protected synthetic workspaces; deterministic plan/apply, fail-closed cases, and history preservation | Real target selection, policy, authenticated review, signatures, external invalidation, aliases, and public recovery are not implemented by the drill |
| [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Substantive repository-grounded draft | Defect classification, containment/referral, rollback-versus-withdrawal decision model, synthetic capability map, and operational graduation gate | Production rollback pipeline and published-alias auditor remain placeholders; operational rollback and public recovery remain held |

Document maturity is not operational admission. Each row must be re-read when its pinned dependency, workflow, validator, fixture, candidate, policy, or runtime surface changes.

[Back to top](#top)

---

<a id="current-capability-and-hold-map"></a>

## Current capability and hold map

| Surface | Current bounded state | Safe conclusion |
|---|---|---|
| Hazards runbook lane boundary | **SUBSTANTIVE on this stacked branch** | Six child procedures are indexed and their terminal boundaries are explicit |
| Drought-family schema and fixture validation | **IMPLEMENTED BOUNDED** | Exact committed valid/invalid fixture polarity can be checked without live source access |
| USDM materiality evaluation | **IMPLEMENTED BOUNDED** | Deterministic synthetic materiality outcomes can be tested; they are not source or release decisions |
| Synthetic rollback and withdrawal mechanics | **IMPLEMENTED BOUNDED** | Marker-protected temporary workspaces can be planned or mutated with preservation and negative-case checks |
| Live Hazards source authority | **ABSENT / HOLD** | The current source-authority projection does not activate a source |
| Live connector and refresh execution | **CONFLICTED / UNVERIFIED / HOLD** | No accepted live Hazards refresh command or operational connector path is established |
| EvidenceBundle and proof production | **HOLD** | Domain workflow readiness jobs do not establish proof closure |
| Active Hazards policy evaluation | **NEEDS VERIFICATION / HOLD** | Default or draft policy source is not an accepted runtime evaluator result |
| Hazards release candidate | **ABSENT** | No candidate can be promoted or released |
| Promotion execution and release authority | **UNKNOWN / HOLD** | Readiness validation cannot create an authenticated decision or apply a transition |
| Operational rollback and external invalidation | **PLACEHOLDER / HOLD** | Synthetic invalidation records do not call real caches, tiles, catalogs, indexes, APIs, or deployments |
| Deployed public read-back and recovery | **UNKNOWN** | Do not claim runtime, deployment, release, rollback, or publication maturity |
| KFM as life-safety authority | **DENY** | No document, transform, reviewer, or future implementation may convert KFM into the issuing authority for emergency instructions |

[Back to top](#top)

---

<a id="shared-hazards-operating-invariants"></a>

## Shared Hazards operating invariants

Every procedure in this directory preserves the following rules:

1. **Not for life safety.** Operational warnings, watches, advisories, declarations, and incident messages remain attributed context from an identified official source. KFM does not originate protective-action guidance.
2. **Source-role anti-collapse.** Historical event, observation, forecast, model, regulatory area, administrative declaration, warning context, synthetic fixture, exposure summary, and resilience interpretation remain distinguishable.
3. **Time is part of meaning.** Issue, observation, effective, validity, expiry, cancellation, supersession, correction, retrieval, transaction, and release time remain separate where material. A recent retrieval does not prove a product is current.
4. **Cite or abstain.** An evidence-dependent claim resolves its required `EvidenceRef` to admissible support or returns a finite abstention, denial, error, or hold appropriate to the owning contract and policy.
5. **Public clients cross the trust membrane.** Maps, Evidence Drawer, Focus Mode, exports, dashboards, and APIs use governed interfaces and released public-safe carriers, never RAW, WORK, QUARANTINE, canonical/internal stores, private links, or direct model output.
6. **Representation is not truth.** Tiles, symbology, dashboards, screenshots, indexes, summaries, graph projections, model outputs, and AI language are downstream carriers whose limitations and transforms remain visible.
7. **Promotion is a governed state transition.** Validation, review, decision, transition application, release, deployment, promotion, publication, correction, withdrawal, and rollback are separate events.
8. **Corrections preserve lineage.** Do not erase or silently rewrite affected release history. Record supersession, correction, withdrawal, invalidation, and rollback relationships through their owning objects.
9. **Unknowns fail closed in proportion to consequence.** Missing authority, rights, sensitivity, time, evidence, target identity, reviewer assignment, or rollback support cannot be upgraded through plausible prose.

[Back to top](#top)

---

<a id="procedure-sequencing-and-state-separation"></a>

## Procedure sequencing and state separation

### Public or consequential surface change

1. Pin the exact revision, artifact, route, view, layer, prompt, or export.
2. Run the not-for-life-safety audit against the exact rendered or machine-consumed result.
3. Run the applicable bounded validation profile.
4. Record unresolved evidence, time, rights, sensitivity, policy, accessibility, referral, release, and correction joins.
5. Stop at a public-safe review handoff. A documentation review cannot authorize exposure.

### Source change or refresh proposal

1. Use the source-refresh runbook to freeze source identity, authority, descriptor, rights, cadence, connector, and pipeline paths.
2. Run the no-network validation profile; do not substitute live retrieval for missing fixtures or acceptance.
3. Keep new or uncertain input in the owning RAW or QUARANTINE procedure until source admission and validation support a later transition.
4. Use the promotion runbook only after an immutable candidate and all required support actually exist.
5. Keep release, deployment, and publication as separate governed work.

### Released or release-facing defect

1. Fail closed and preserve official-source referral where users could be misled.
2. Freeze the affected release, carrier, scope, evidence, time, correction, consumer, and current public state.
3. Use the rollback runbook to choose rollback, withdrawal, forward correction, or hold.
4. Use the rollback drill only for the tracked marker-protected synthetic rehearsal. Never aim the helper at a real release.
5. Require separately authorized execution, invalidation, public read-back, correction lineage, and closure evidence before claiming recovery.

### States that must not be collapsed

| Earlier state | Does not imply |
|---|---|
| File exists | Procedure is current, correct, rehearsed, or operationally admitted |
| Schema or fixture passes | Source is true, evidence is resolved, or policy approved |
| Validator returns `PASS` | Human review, decision, transition, release, deployment, or publication occurred |
| Pull request merges | Candidate, release, deployment, promotion, or public state changed |
| Synthetic rehearsal passes | A real target is safe or operational recovery succeeded |
| Manifest-shaped or RollbackCard-shaped file exists | Authenticated authority or execution exists |
| Public layer is visible | Carrier is evidence-complete, policy-approved, current, or safe for consequential use |

[Back to top](#top)

---

<a id="validation-and-rehearsal-entry-points"></a>

## Validation and rehearsal entry points

Run commands from the repository root at a recorded 40-character commit SHA. Re-read each named runbook before use; these commands do not supersede its preconditions or stop conditions.

### Bounded Hazards validation

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC \
  python -m unittest -v \
  tests.domains.hazards.test_hazards_smoke

KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC \
  make hazards-validate
```

### Bounded synthetic rollback rehearsal

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC \
  python -m unittest -q \
  tests.release.test_synthetic_rollback_rehearsal \
  tests.domains.hazards.test_synthetic_rollback_rehearsal

python tools/validators/release/validate_rollback_card.py --fixtures
```

### Shared promotion-readiness validation

```bash
make publish-check
```

A green result is bounded to the selected profile. It does not establish live source fitness, evidence truth, active policy, completed review, candidate assembly, release authority, operational rollback, deployment, promotion, or publication.

### Documentation validation

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  docs/runbooks/hazards/
```

The link checker validates repository-local targets and bounded fragments. It does not validate external availability, procedure semantics, citations, authority, operational safety, or implementation maturity.

### Hosted orchestration

- [`domain-hazards`](../../../.github/workflows/domain-hazards.yml) runs bounded Hazards validation and retains explicit proof/release holds.
- [`rollback-drill`](../../../.github/workflows/rollback-drill.yml) inspects the bounded rollback-card and synthetic-rehearsal surfaces while retaining production holds.
- Generic documentation workflows may validate metadata, local links, and document structure.

A successful held job is evidence that the declared hold remained intact. It is not proof that the held capability exists.

[Back to top](#top)

---

<a id="mandatory-stop-conditions"></a>

## Mandatory stop conditions

Stop and record `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, or `NEEDS VERIFICATION` according to the owning procedure when any applicable condition below is present:

- KFM-authored or KFM-presented content issues or appears to issue protective-action guidance, current warning interpretation, an evacuation or shelter direction, medical advice, an all-clear, safe-return assurance, or another life-safety instruction;
- an official issuer, source role, record identity, observation/issue time, validity, expiry, cancellation, supersession, correction, retrieval time, or currentness state cannot be established;
- stale, expired, cancelled, superseded, corrected, conflicting, missing, modeled, or synthetic support would be shown as current observation or authoritative instruction;
- required evidence cannot resolve, generated language outranks evidence, or a map, tile, index, dashboard, model, or AI answer is treated as canonical truth;
- rights, redistribution terms, sensitivity, precision, sovereignty, living-person information, critical infrastructure, protected locations, credentials, or private access remain unresolved;
- a public path would read RAW, WORK, QUARANTINE, canonical/internal state, a private link, an unsigned mutable artifact, or direct model output;
- the requested step would contact or activate a live source, write external state, use credentials, mutate lifecycle or public state, change repository settings, release, deploy, promote, publish, or invalidate production consumers without the separately governed authority and accepted implementation required for that transition;
- a candidate, prior safe target, correction notice, rollback target, accountable reviewer, policy result, release authority, invalidation consumer, or public read-back path is absent or unverified;
- the command, path, workflow, contract, schema, fixture, validator, policy, or procedure does not match the pinned repository revision; or
- overlapping work owns the same path or semantics and has not been reconciled.

Do not weaken a negative case, disable a guard, substitute an illustrative example, or broaden a fixture merely to obtain a passing result.

[Back to top](#top)

---

<a id="authority-ownership-and-handoff"></a>

## Authority, ownership, and handoff

`@bartytime4life` is the verified GitHub review route. That routing does not authenticate an emergency-management authority, scientific steward, source-rights reviewer, sensitivity reviewer, policy approver, release authority, rollback executor, operations owner, or independent reviewer.

Before acting on a runbook result:

1. identify the exact actor, role, scope, effective interval, obligations, and revocation path required by the transition;
2. resolve the governing contract, schema, policy, evidence, review, lifecycle, release, correction, and rollback records from their owning roots;
3. preserve finite outcomes exactly as emitted; do not translate `PASS`, `APPROVE_READY`, a green held job, or a review note into a stronger state;
4. keep source admission, validation, review, decision, transition application, release, deployment, promotion, rollback execution, publication, and public read-back as separate evidence events; and
5. produce a public-safe handoff rather than copying credentials, protected payloads, precise restricted locations, exploit details, or private review text into documentation.

### Minimum handoff record

```yaml
repository_sha: <40-character SHA>
selected_procedure: <repository path>
change_or_incident_scope: <bounded scope>
input_identity:
  object_or_artifact_ref: <stable reference>
  digest_or_version: <value or NEEDS VERIFICATION>
source_and_time:
  source_role: <role or unresolved>
  observed_or_issued_at: <timestamp or not applicable>
  valid_or_expires_at: <timestamp or not applicable>
validation:
  commands: []
  finite_outcomes: []
  exact_head_or_candidate_identity: <identity>
remaining_holds: []
authority_and_review:
  requested_roles: []
  completed_records: []
correction_and_rollback:
  affected_release_ref: <ref or not applicable>
  correction_ref: <ref or NEEDS VERIFICATION>
  rollback_or_withdrawal_target: <ref or NEEDS VERIFICATION>
non_effects:
  source_activated: false
  lifecycle_mutated: false
  release_executed: false
  deployment_executed: false
  promotion_executed: false
  publication_executed: false
```

Use the exact schema or accepted record type when one exists. This worksheet is a human handoff aid, not a substitute authority object.

[Back to top](#top)

---

<a id="open-verification-and-missing-procedures"></a>

## Open verification and missing procedures

| Item | Current posture | Smallest truthful next step |
|---|---|---|
| Accountable roles and separation of duties | **NEEDS VERIFICATION** | Record accepted assignments with scope, authority, effective interval, obligations, and revocation; do not treat CODEOWNERS as release authority |
| Hazards source authority and canonical descriptor path | **ABSENT / CONFLICTED / HOLD** | Reconcile the empty projection, duplicate registry homes, descriptor fields, connector paths, rights, cadence, and activation decision before a live refresh |
| Live connector and pipeline implementation | **UNVERIFIED / HOLD** | Admit one bounded source through an accepted connector, fixture set, negative tests, no-network replay, receipts, and lifecycle handoff before live execution |
| Active policy evaluator and governed consumer binding | **NEEDS VERIFICATION / HOLD** | Demonstrate an accepted policy bundle, exact evaluator identity, obligations, negative tests, and consumer enforcement at a pinned revision |
| EvidenceBundle, proof, and catalog closure | **HOLD** | Close one public-safe fixture circle from stable identity through evidence, policy/review, governed API, map/Evidence Drawer, and correction/rollback demonstration |
| Hazards candidate and operational promotion | **ABSENT / HOLD** | Assemble one immutable candidate only after source, evidence, rights, sensitivity, validation, policy, review, correction, and rollback prerequisites exist |
| Production rollback, alias audit, invalidation, and public recovery | **PLACEHOLDER / HOLD** | Define accepted interfaces, authenticated authority, dry-run/no-write tests, receipts, partial-failure behavior, public read-back, and reversal before operational use |
| Dedicated correction, release, validation, or stale-state child runbooks | **NOT TRACKED IN THIS DIRECTORY** | Use the current audit, source-refresh, promotion, rollback, and owning release/lifecycle surfaces; create another file only after a repository-grounded need and placement review |
| Parent runbook inventory | **HISTORICAL SNAPSHOT** | Reconcile `docs/runbooks/README.md` after this stacked change lands so it no longer describes Hazards as a one-byte placeholder |

A missing local procedure does not authorize improvisation. Use the closest accepted cross-domain runbook or owning responsibility surface and record the gap.

[Back to top](#top)

---

<a id="related-responsibility-surfaces"></a>

## Related responsibility surfaces

### Governing and domain documentation

- [Parent operational-procedure index](../README.md)
- [Hazards domain boundary](../../domains/hazards/README.md)
- [Hazards life-safety boundary](../../domains/hazards/LIFE_SAFETY_BOUNDARY.md)
- [Hazards publication and public-boundary guidance](../../domains/hazards/PUBLICATION_AND_BOUNDARY.md)
- [Directory Rules v2](../../doctrine/directory-rules.md)
- [ADR-0029 — adopt Directory Governance Standard v2](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)

### Source, policy, release, and executable boundaries

- [Source-authority projection](../../../control_plane/source_authority_register.yaml)
- [Hazards policy boundary](../../../policy/domains/hazards/README.md)
- [Hazards release-candidate lane](../../../release/candidates/hazards/README.md)
- [Release governance root](../../../release/README.md)
- [General synthetic rollback rehearsal](../rollback-rehearsal.md)
- [RollbackCard contract](../../../contracts/release/rollback_card.md)
- [RollbackCard schema](../../../schemas/contracts/v1/release/rollback_card.schema.json)
- [Synthetic rollback helper](../../../tools/release/rollback_apply.py)
- [Generic rollback rehearsal tests](../../../tests/release/test_synthetic_rollback_rehearsal.py)
- [Hazards rollback rehearsal tests](../../../tests/domains/hazards/test_synthetic_rollback_rehearsal.py)

[Back to top](#top)

---

<a id="maintenance-correction-and-document-rollback"></a>

## Maintenance, correction, and document rollback

Update this README when:

- a child runbook is added, removed, renamed, superseded, or materially changes its scope or terminal boundary;
- a bounded fixture or validator graduates, regresses, or changes its finite outcomes;
- live source authority, a connector, pipeline, policy evaluator, EvidenceBundle resolver, proof producer, candidate assembler, promotion executor, release topology, rollback executor, invalidation adapter, deployment, or public read-back becomes verified;
- the Hazards/Atmosphere/Hydrology/Settlements/Roads seam changes;
- accountable ownership or separation of duties is accepted or revoked;
- a real incident, exercise, correction, withdrawal, or rollback exposes a procedure gap; or
- the stacked dependency or parent inventory is reconciled.

This is a documentation-only change. Before merge, close or abandon its draft pull request and branch through normal repository controls. After an authorized merge, revert the focused documentation commit or submit a smaller reviewed forward correction. Reverting this README does not alter source descriptors, connectors, fixtures, validators, policy, evidence, lifecycle data, candidates, release records, aliases, deployments, public carriers, or publication state.

[Back to top](#top)
